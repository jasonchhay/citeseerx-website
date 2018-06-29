from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'psuwebsite/index.html')

def privacy_policy(request):
    return render(request, 'psuwebsite/privacy-policy.html')

def help(request):
    return render(request, 'psuwebsite/help.html')