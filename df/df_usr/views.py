#coding=utf-8

"""
df_usr:views
urls必须对应一个模板，否则会出现错误提示。

if后面没有：会报错，提示 invalid syntax 
如果if里面没有语句会提示预付错误 SyntaxError，找不到变量也会有这个提示

== 写成 = 
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
    try:
        user = UsrInfo.objects.get(uname=uname)
    except:
        return redirect("/user/info/")
    else:
        if upwd == user.upwd:
            return redirect("/")

def register(request):
    
    return redirect("/user/info/")



def info(request):
    return render(request,"df_usr/user_center_info.html")
