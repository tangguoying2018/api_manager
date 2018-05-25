#!/usr/bin/env python
# coding: utf-8
# author: tang

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_class/', views.new_class, name='new_class'),
    url(r'^new_api/', views.new_api, name='new_api'),
    url(r'^edit_api/', views.edit_api, name='edit_api'),
    url(r'^del_api/', views.del_api, name='del_api'),
    url(r'^copy_api/', views.copy_api, name='copy_api'),
    url(r'^edit_class/', views.edit_class, name='edit_class'),
    url(r'^del_class/', views.del_class, name='del_class'),
    url(r'^class_detail/', views.class_detail, name='class_detail'),
]

handler404 = views.page_not_found
handler500 = views.page_error