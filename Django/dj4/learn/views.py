# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(u'Hello ShiYanLou!')


def home(request):
    string = u'There are some cources:'
    TutorialList = ['html', 'css', 'dajngo', 'python', 'javascript',]
    return render(request, 'home.html', {'TutorialList': TutorialList})

