from django.urls import path
from . import views

urlpatterns = [
    path('data', views.data, name = 'data'), 

    path('software', views.software, name = 'software')
]
