from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TeamMember

def team(request):
    coreteam = TeamMember.objects.all().filter(category = 'Core Team')
    contributors = TeamMember.objects.all().filter(category = 'Noted Contributors')
    founders = TeamMember.objects.all().filter(category = 'Founders')
    return render(request, 'psuwebsite/team.html', {'coreteam':coreteam,
                                                    'contributors': contributors,
                                                    'founders':founders})