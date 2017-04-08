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
from django.http import HttpResponseRedirect
from df_usr.models import *
from df_usr.usr_wrap import *



# Create your views here.

def login(request):
    uname=request.COOKIES.get('uname','')
    context = {"uname":uname}
    return render(request,"df_usr/login.html", context)

def login_handle(request):
    # 查询用户最近的跳转地址，如果没有默认为根目录
    url=request.COOKIES.get('url','/')
    # 构造最近跳转地址的Response对象
    red = HttpResponseRedirect(url)


    #获得玩家post提交信息
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
        print(url)
        # 成功登陆后设置cookie中的url为空，保存时间为-1秒，即立即删除
        red.set_cookie("url",'',max_age=-1)

        if static != 0:
            red.set_cookie('uname',uname)
        else:
            red.set_cookie('uname','',max_age=-1)
        #登陆成功记录用户的登陆状态，使用session进行记录，在request中进行设置
        request.session['user_id']=user.id
        request.session['user_name']=uname
    finally:
       return red



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
@login_check
def info(request):
    user_id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=user_id)

    context = {"title":"个人信息","tyle":1,"user":user}
    return render(request,"df_usr/user_center_info.html",context)

#订单信息    
@login_check
def order(request):
    context = {"title":"订单信息","tyle":2}
    return render(request,"df_usr/user_center_order.html",context)
#收货地址
@login_check
def site(request):
    user_id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=user_id)

    messages = request.GET
    if messages.get("ushou",0):
        user.ushou = messages.get("ushou")
        user.uaddress = messages.get("uaddress")
        user.uyoubian = messages.get("uyoubian")
        user.uphone = messages.get("uphone")
        user.save()

    context = {"title":"收货信息","user":user}
    return render(request,"df_usr/user_center_site.html",context)


