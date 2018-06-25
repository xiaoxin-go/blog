from django.shortcuts import render
from django.http import JsonResponse
from BlogPro.models import *
import math

# Create your views here.
#返回主页数据
def index(request):
    ContentList = TContent.objects.filter(type=0).order_by('-addTime')[:5]
    reSetData.tab(ContentList)
    ContentTop = TContent.objects.filter(type=1)[0]
    Link = TLink.objects.filter(isdelete=1)
    Image = TImage.objects.filter(isdelete=1)
    title = '个人博客'
    return render(request, 'blog/index.html', locals())

#返回文章页面数据
def content(request,index):
    ContentList = TContent.objects.filter(isdelete=1,type=0).order_by('-addTime')
    Link = TLink.objects.filter(isdelete=1)
    if not index:
        page = [i for i in range(1,math.ceil(len(ContentList)/6)+1)]
        ContentList = ContentList[:6]
        reSetData.tab(ContentList)
        print(page)
        title = '文章'
        text = '想要得到自己想要的生活，唯有努力坚持'
        return render(request, 'blog/article.html', locals())
    else:
        i = (int(index)-1)*6
        ContentList = ContentList[i:i+6]
        dataList = reSetData(ContentList).content()
        return JsonResponse(dataList,safe=False)

def mood(request,index):
    contentList = TMood.objects.all().order_by('-addTime')
    count = contentList.count()
    if not index:
        title = '说说'
        text = '存在于身边的事物，如果不经常留意的话，反而会由于太过接近而容易失去'
        page = list(range(1,math.ceil(count/10)+1))
        contentList = contentList[:10]
        html = 'blog/moodList.html'
    else:
        i = (int(index)-1)*10
        contentList = contentList[i:i+10]
        html = 'blog/moodcontent.html'
    return render(request,html,locals())

def commit(request):
    title = '留言'
    text = '或许生活真的需要用心去体检，体检感情，体检工作，体会生活，不管什么事，只要拿起勇气去面对，不去在意别人的眼光，做好最好的自己'
    return render(request, 'blog/commit.html', locals())

#返回文章内容数据
def text(request,id):
    if id:
        content = TContent.objects.get(id=id)
        title = content.title
        try:
            ContentList = TContent.objects.filter(type=0).order_by('-addTime')[:5]
            prev = Prev(int(id)) or ''
            next = Next(int(id)) or ''
            Link = TLink.objects.filter(isdelete=1)
            label = content.label.split(',')
            context = content.content.split('\n')
        except Exception as e:
            print(e)
        else:
            return render(request, 'blog/article_detail.html', locals())
        finally:
            content.read += 1
            content.save()

#寻找上一篇文章
def Prev(id):
    for id in range(id-1,0,-1):
        content = TContent.objects.filter(id=id,isdelete=1)
        if content:
            return content[0]

#寻找下一篇文章
def Next(id):
    len = TContent.objects.all().count()
    for id in range(id+1,len+1):
        content = TContent.objects.filter(id=id,isdelete=1)
        if content:
            return content[0]

#重置数据
class reSetData:
    def __init__(self,ContentList):
        self.ContentList = ContentList
    #重置返回的数据
    def content(self):
        dataList = []
        for item in self.ContentList:
            data = {}
            data['title'] = item.title
            data['user'] = item.user
            data['read'] = item.read
            data['review'] = item.review
            data['addTime'] = item.addTime
            data['content'] = item.content
            data['label'] = item.label
            dataList.append(data)
        return dataList

    #重置lab方法
    @classmethod
    def tab(cls,ContentList):
        for content in ContentList:
            content.label = content.label.split(',')