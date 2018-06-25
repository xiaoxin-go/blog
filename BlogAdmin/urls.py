from django.conf.urls import url,include
from BlogAdmin import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$',views.login,name='login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^article/(\d*)$',views.article,name='article'),
    url(r'^notice/$',views.notice,name='notice'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^commit/$',views.commit,name='commit'),
    url(r'^category/$',views.category,name='category'),
    url(r'^flink/$',views.flink,name='flink'),
    url(r'^manageUser/$',views.manageuser,name='manageuser'),
    url(r'^loginlog/$',views.loginlog,name='loginlog'),
    url(r'^setting/$',views.setting,name='setting'),
    url(r'^readset/$',views.readset,name='readset'),

]