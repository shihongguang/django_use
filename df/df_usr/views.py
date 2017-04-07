#coding=utf-8

"""
df_usr:views
"""


from django.shortcuts import render

# Create your views here.

def info(request):
    return render(request,"df_usr/user_center_info.html")
