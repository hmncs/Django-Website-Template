# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:44:13 2021

@author: mende
"""


from django.urls import path

from . import views

urlpatterns = [
    path('', views.service_index, name='service_index'),
    path('<int:service_id>/', views.service_view, name='service'),
]