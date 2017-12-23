from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'psuwebsite/index.html')

def people(request):
    return render(request, 'psuwebsite/people.html')