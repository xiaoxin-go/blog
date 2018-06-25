from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from BlogAdmin.models import TUser
from BlogPro.models import TContent,TLink,TMood,TComment
import hashlib
import time
import math

def now():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

def login(request):
    return render(request,'admin/login.html')

@csrf_exempt
def index(request):
    if request.method == 'POST':
        requests = request.POST
        name = requests['uname']
        pwd = requests['pwd']
        print(name,pwd)
        user = TUser.objects.filter(name=name)
        if user:
            user = user[0]
            if MD5(pwd) == user.pwd:
                user.count += 1
                user.save()
                request.session['uname'] = name
                data = indexdata(name)
                user.previp = user.loginip
                user.loginip = request.META['REMOTE_ADDR']
                user.logintime = now()
                user.save()
                return render(request, 'admin/index.html',locals())
        return render(request,'admin/login.html',{'msg':'用户名或密码不正确'})
    uname = request.session.get('uname')
    if not uname:
        return redirect('/admin/login/')
    data = indexdata(uname)
    return render(request,'admin/index.html',locals())

def indexdata(uname):
    user = TUser.objects.get(name=uname)
    data = {}
    data['count'] = user.count
    data['countall'] = TUser.objects.all().count()
    data['logintime'] = user.logintime
    data['previp'] = user.previp
    data['contentcount'] = TContent.objects.all().count()
    data['commentcount'] = TComment.objects.all().count()
    data['linkcount'] = TLink.objects.all().count()
    return data


def article(request,index):
    index = int(index) or 1
    contents = TContent.objects.all()
    count =contents.count()
    indexlist = list(range(1,math.ceil(count/8)+1))
    c = (index-1)*8
    contents = contents[c:c+8]
    prev = index - 1
    next = index + 1
    last = indexlist[-1]
    return render(request,'admin/article.html',locals())

def notice(request):
    return render(request,'admin/notice.html',locals())

def comment(request):
    return render(request,'admin/comment.html',locals())

def commit(request):
    return render(request,'admin/commit.html',locals())

def category(request):
    return render(request,'admin/category.html',locals())

def flink(request):
    return render(request,'admin/flink.html',locals())

def manageuser(request):
    return render(request,'admin/manageuser.html',locals())

def loginlog(request):
    return render(request,'admin/loginlog.html',locals())

def setting(request):
    return render(request,'admin/setting.html',locals())

def readset(request):
    return render(request,'admin/readset.html',locals())

def MD5(str):
    h = hashlib.md5()
    h.update(str.encode(encoding='utf-8'))
    return h.hexdigest()