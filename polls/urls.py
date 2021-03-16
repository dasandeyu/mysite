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
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/results/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
