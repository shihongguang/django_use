#coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail_list/(\d)$', views.detail_list),
    url(r'^detail/(\d)/$', views.detail),
    #添加搜索的配置
    url(r'^search/', include('haystack.urls')),
    url(r'^query/', views.query),
]
