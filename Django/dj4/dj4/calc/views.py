# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        #when form use post method
        form = AddForm(request.POST)
        if form.is_valid():
            #if the data is valid
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        #when use usual
        form = AddForm()
    
    return render(request, 'index.html', {'form': form})


def add(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
