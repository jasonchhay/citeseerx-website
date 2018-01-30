from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog(request):
    blogs = Blog.objects.all().filter().order_by('-date')
    return render(request, 'psuwebsite/Blog.html', {'blogs': blogs})