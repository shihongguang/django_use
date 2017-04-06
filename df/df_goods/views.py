#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *
from django.core.paginator import Paginator



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

def detail(request,t):
    p = int(request.GET.get("page",1))
    good_type = TypeInfo.objects.get(id=t)
    list_id = good_type.goodsinfo_set.order_by("-id")[:3]
    list_click = good_type.goodsinfo_set.order_by("-gclick")

    list_click_p = Paginator(list_click, 20) 
    list_page = list_click_p.page_range

    click = list_click_p.page(p)    
    

    context = {"title":"商品列表","id":list_id,"click":click,"pages":list_page,
                "prev_page":p-1,"next_page":p+1,"t":t,"p":p
            }

    return render(request, "df_goods/list.html",context)


