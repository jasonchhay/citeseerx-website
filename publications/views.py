from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.


def publications(request):
    return render(request, 'psuwebsite/publications.html')