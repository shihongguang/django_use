#coding=utf-8

"""
df_usr:urls
如果这个页面的urls配置错误会影响其他页面的显示
"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^user/info/$',views.info),

]