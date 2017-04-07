from django.conf.urls import include, url
from django.contrib import admin
from . import views

"""
cart:urls
"""


urlpatterns = [
    url(r'^cart/$', views.cart),
]
