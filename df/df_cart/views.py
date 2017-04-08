#coding=utf-8

"""
如果异步请求时，无法检查错误，可以直接使用地址请求查看错误。
django使用数据库储存数据时，不用转换数据的类型，直接付给对象就可以。

字段中储存的是外键，要给外键加值时，使用字段_id,给这个字段进行赋值。或者给他加对应的对象

"""
from django.shortcuts import render,redirect
from django.http import JsonResponse

from df_cart.models import *

def cart(request):
    uid=request.session['user_id']
    carts=CartInfo.objects.filter(user_id=uid)
    context={'title':'购物车',
             'carts':carts}
    return render(request,'df_cart/cart.html',context)

def add_cart(request):
    user_id = request.session.get("user_id")
    news = request.GET
    gid = news.get("id")
    gid = int(gid)
    count = news.get("num")
    count = int(count)

    carts = CartInfo.objects.filter(user_id=user_id,goods_id=gid)
    if len(carts)>=1:
        cart_info=carts[0]
        cart_info.count=cart_info.count+count
    else:
        cart_info = CartInfo()
        cart_info.user_id = user_id
        cart_info.goods_id = gid
        cart_info.count = count

    cart_info.save()
    #如果是ajax请求则返回json，否则转向购物车,这个地方不是自己写的
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=user_id).count()
        return JsonResponse({'cart_id':cart_info.id,'count':count})
    else:
        return redirect('/cart/')