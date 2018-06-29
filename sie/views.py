from django.shortcuts import render

# Create your views here.
def scholarly_information_extraction(request):
    return render(request, 'psuwebsite/scholarly-information-extraction.html')