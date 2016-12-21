# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here. hello
def index(request):
    # 另外一种方法，使用render
    # render()函数将请求对象作为它的第一个参数，模板的名字作为它的第二个参数，一个字典作为它可选的第三个参数。 它返回一个HttpResponse对
    # 象，含有用给定的context 渲染后的模板
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    contex = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', contex)


def detail(request, question_id):
    print "question_id =", question_id
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
