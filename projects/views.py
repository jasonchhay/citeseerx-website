from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Projects
# Create your views here.


def projects(request):
    projects = Projects.objects.all().filter().order_by('-year')

    return render(request, 'psuwebsite/projects.html', {'projects': projects})