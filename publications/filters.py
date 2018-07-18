from .models import Publication
import django_filters

class PublicationFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author=django_filters.CharFilter(field_name = 'author', lookup_expr='icontains')
    year__gte= django_filters.NumberFilter(field_name='year',lookup_expr='gte')
    year__lte=django_filters.NumberFilter(field_name='year',lookup_expr='lte')
    venue=django_filters.CharFilter(field_name='venue', lookup_expr='icontains')
    category = django_filters.MultipleChoiceFilter(field_name='category', choices=(('Journal','Journal Papers'),('Conference','Conference Papers')))

    class Meta:
        model = Publication
        '''
        fields = {'title':['icontains',] ,
                  'author':['icontains', ],
                  'year':['exact','gte','lte', ],
                  'venue':['icontains', ],
                  'category':['exact']}
        '''

        fields = ['title','author', 'year__gte', 'year__lte', 'venue', 'category']
