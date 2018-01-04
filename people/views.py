from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Professor, CurrentTeam, alumni


def people(request):
    professors = Professor.objects.all().filter().order_by('id')
    undergraduate = CurrentTeam.objects.all().filter(occupation='Undergraduate')
    postdoc = CurrentTeam.objects.all().filter(occupation = 'Postdoc')
    phdstudent = CurrentTeam.objects.all().filter(occupation = 'PhD Student')
    master = CurrentTeam.objects.all().filter(occupation = 'Masters Student')
    staff = CurrentTeam.objects.all().filter(occupation = 'Staff')
    undergraduatealumni = alumni.objects.all().filter(occupation = "Undergraduate")
    postdocalumni = alumni.objects.all().filter(occupation='Postdoc')
    phdstudentalumni = alumni.objects.all().filter(occupation='PhD Student')
    masteralumni = alumni.objects.all().filter(occupation='Masters Student')
    staffalumni = alumni.objects.all().filter(occupation='Staff')
    return render(request, 'psuwebsite/people.html', {'professors': professors,
                                                      'undergraduates': undergraduate,
                                                      'postdocs': postdoc,
                                                      'phdstudents': phdstudent,
                                                      'masters': master,
                                                      'staffs': staff,
                                                      'undergraduatesalumni': undergraduatealumni,
                                                      'postdocsalumni': postdocalumni,
                                                      'phdstudentsalumni': phdstudentalumni,
                                                      'mastersalumni': masteralumni,
                                                      'staffsalumni': staffalumni
                                                      })


def professors(request):
    professors = Professor.objects.all().filter().order_by('id')
    return render(request, 'psuwebsite/professors.html', {'professors': professors})

def postdocs(request):
    postdoc = CurrentTeam.objects.all().filter(occupation = 'Postdoc')
    return render(request, 'psuwebsite/postdoc.html', {'postdocs': postdoc})

def phdstudents(request):
    phdstudent = CurrentTeam.objects.all().filter(occupation = 'PhD Student')
    return render(request, 'psuwebsite/phdstudent.html', {'phdstudents': phdstudent})

def master(request):
    master = CurrentTeam.objects.all().filter(occupation = 'Masters Student')
    return render(request, 'psuwebsite/master.html', {'masters': master})

def undergraduate(request):
    undergraduate = CurrentTeam.objects.all().filter(occupation='Undergraduate')
    return render(request, 'psuwebsite/undergraduate.html', {'undergraduates': undergraduate})

def staff(request):
    staff = CurrentTeam.objects.all().filter(occupation = 'Staff')
    return render(request, 'psuwebsite/staff.html', {'staffs': staff})

def alumni1(request):
    undergraduatealumni = alumni.objects.all().filter(occupation = "Undergraduate")
    postdocalumni = alumni.objects.all().filter(occupation='Postdoc')
    phdstudentalumni = alumni.objects.all().filter(occupation='PhD Student')
    masteralumni = alumni.objects.all().filter(occupation='Masters Student')
    staffalumni = alumni.objects.all().filter(occupation='Staff')
    return render(request, 'psuwebsite/alumni.html', {'undergraduatesalumni': undergraduatealumni,
                                                      'postdocsalumni': postdocalumni,
                                                      'phdstudentsalumni': phdstudentalumni,
                                                      'mastersalumni': masteralumni,
                                                      'staffsalumni': staffalumni})