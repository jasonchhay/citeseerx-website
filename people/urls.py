from django.urls import path
from . import views


urlpatterns = [
    path('', views.people, name = 'people'),

    path('professors', views.professors, name = 'professors'),

    path('PostDocs', views.postdocs, name = 'PostDocs'),

    path('Phd_students', views.phdstudents, name = 'Phd_students'),

    path('Master', views.master, name = 'master'),

    path('Undergraduates', views.undergraduate, name = 'undergraduates'),

    path('Staff', views.staff, name = 'staff'),

    path('Alumni', views.alumni1, name='alumni')


]