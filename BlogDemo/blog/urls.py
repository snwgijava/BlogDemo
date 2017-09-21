# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 23:11
# @Author  : yj

from django.conf.urls import url

from . import views


app_name='blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivewView.as_view(),name='archives'),
    url(r'^archives/$',views.ArchivewView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
    # url(r'^search/$',views.search,name='search'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
]