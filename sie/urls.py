from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarly_information_extraction, name = 'scholarly-information-extraction')
]