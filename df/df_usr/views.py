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
from df_usr.usr_wrap import *



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
        user = UserInfo.objects.get(uname=uname)
    except Exception as e:
        print ("error info",e)
        return redirect("/user/login/")
    else:
        print(user)
    
    return redirect("/")



def register(request):
    return render(request,"df_usr/register.html") 

def register_handle(request):
    #post方法
    #html中的跳转路径必须时/user/register_handle/，没有最后的/会报错
    news = request.POST
    uname=news.get('user_name')
    upwd=news.get('pwd')
    upwd2=news.get('cpwd')
    uemail=news.get('email')
    #判断两次密码
    if upwd!=upwd2:
        return redirect('/user/register/')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()
    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    #注册成功，转到登录页面
    return redirect('/user/login/')

#个人信息
def info(request):
    return render(request,"df_usr/user_center_info.html")

def order(request):
    return render(request,"df_usr/user_center_order.html")
#收货地址
@login_check
def site(request):
    return render(request,"df_usr/user_center_site.html")
