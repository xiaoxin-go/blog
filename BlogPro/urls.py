from django.conf.urls import url
from BlogPro import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^content/(\d*)$',views.content),
    url(r'^content/getText/(\d*)$',views.text),
    url(r'^moodList/(\d*)$',views.mood),
    url(r'^commit$',views.commit)
]