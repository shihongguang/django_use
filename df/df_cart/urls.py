from django.conf.urls import include, url
from django.contrib import admin
from . import views

"""
cart:urls
"""


urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^add_cart/$', views.add_cart),
    url(r'^cart/edit(\d+)_(\d+)/$',views.edit),
    url(r'^cart/delete(\d+)/$',views.delete),

]
