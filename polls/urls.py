#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   lanxiang_sh
@License :   (C) Copyright 2020, PayerMax
@Contact :   lanxiang_sh@ushareit.com
@Software:   
@File    :   urls.py
@Time    :   2021/3/2 16:04
@Desc    :
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]