from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Publications
# Create your views here.


def publications(request):
    publications = Publications.objects.all().filter().order_by('-year')
    distinctvenue = Publications.objects.order_by().values_list('venue', flat=True).distinct()
    return render(request, 'psuwebsite/publications.html', {'publications': publications,
                                                            'distinctvenues': distinctvenue})