from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import TeamMember

def team(request):

    for person in TeamMember.objects.all():
        if person.description != None:
            person.description = mark_safe(person.description)

    team = {}
    team['Core Team'] = TeamMember.objects.all().filter(category = 'Core Team')
    team['Noted Contributors'] = TeamMember.objects.all().filter(category = 'Noted Contributors')
    team['Founders'] = TeamMember.objects.all().filter(category = 'Founders')
    return render(request, 'psuwebsite/team.html', {'team' : team})

def collaborators(request):
    return render(request, 'psuwebsite/collaborators.html')