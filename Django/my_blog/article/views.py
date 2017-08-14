# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("Welcome!")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ('title = %s, category = %s, date_time = %s, content = %s'
            % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
