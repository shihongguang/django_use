#coding=utf-8

"""
df_usr:views
urls必须对应一个模板，否则会出现错误提示。
"""
from hashlib import sha1

from django.shortcuts import render,redirect
from df_usr.models import *

# Create your views here.

def login(request):
    return render(request,"df_usr/login.html")
def login_handle(request):
    news = request.POST
    uname = news.get('username')
    upwd = news.get('pwd')
    static = news.get('static',0)
    print(uname,upwd,static)
    UsrInfo



    return redirect("/")



def info(request):
    return render(request,"df_usr/user_center_info.html")
