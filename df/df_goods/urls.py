from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail_list/(\d)$', views.detail_list),
    url(r'^detail/(\d)/$', views.detail),
]
