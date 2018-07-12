from .models import Publication
import django_filters

class PublicationFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields = {'title':['icontains',] ,
                  'author':['icontains', ],
                  'year':['exact','gte','lte', ],
                  'venue':['icontains', ]}
