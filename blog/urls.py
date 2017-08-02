from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^article/(?P<id>[0-9]+)/$',views.article,name = 'article'),
    url(r'^about/$',views.about,name = 'about'),
    url(r'^articlelist/$',views.articleList,name = 'articlelist'),
    url(r'^tags/$',views.taglist,name = 'taglist'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^catagory/$',views.taglist,name='taglist'),
    url(r'^tags/(?P<tag>[0-9]+)/$',views.tags,name='tags')
]