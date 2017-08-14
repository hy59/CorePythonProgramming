from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 15)
def my_view(request):
    return render(request, 'index.html', {'queryset': queryset})