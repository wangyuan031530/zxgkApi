import django_filters
from .models import ZxgkInfo
from django_filters.rest_framework import FilterSet


class ZxgkFilter(FilterSet):
    name = django_filters.CharFilter(field_name='iname', lookup_expr='exact')
    cardnum = django_filters.CharFilter(field_name='cardNum', lookup_expr='exact')

    class Meta:
        model = ZxgkInfo
        fields = ['name', 'cardnum']
