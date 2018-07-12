from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .filters import PublicationFilter
from .models import Publication
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def publications(request):
    publication_list = Publication.objects.all().filter().order_by('-year','title')
    filter = PublicationFilter(request.GET, publication_list)
    paginator = Paginator(filter.qs, 25)

    page = request.GET.get('page')
    
    try:
        publications = paginator.page(page)
    except PageNotAnInteger: 
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)

    print(filter.data)
    return render(request, 'psuwebsite/publications.html', {'publications': publications,
                                                            'filter':filter, 'data':filter.data})

'''
def publications(request):
    return render(request, 'psuwebsite/publications.html', {'publications': Publications.objects.all()})
'''