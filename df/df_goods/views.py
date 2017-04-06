#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *




def index(request):
    list_type = TypeInfo.objects.order_by("id")
    
    list_id_goods = []
    list_click_goods = []

    for goods_type in list_type:
        list_id = goods_type.goodsinfo_set.order_by("-id")[:3]
        list_click = goods_type.goodsinfo_set.order_by("-gclick")[:4] 
        list_id_goods.append(list_id)
        list_click_goods.append(list_click)  

    context = {"title":"首页","id":list_id_goods,"click":list_click_goods}

    return render(request, "df_goods/index.html",context)