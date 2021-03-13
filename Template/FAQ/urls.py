# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:52:43 2021

@author: mende
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]