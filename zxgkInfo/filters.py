import django_filters
from .models import Person
from django_filters.rest_framework import FilterSet


class PersonFilter(FilterSet):
    name = django_filters.CharFilter(field_name='iname', lookup_expr='exact')
    cardnum = django_filters.CharFilter(field_name='cardNum', lookup_expr='exact')
    #category = django_filters.CharFilter(field_name='category', lookup_expr='exact')

    class Meta:
        model = Person
        fields = ['name', 'cardnum']
