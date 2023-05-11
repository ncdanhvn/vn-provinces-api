from django_filters import NumberFilter, BooleanFilter
from django_filters.rest_framework import FilterSet
from .models import Province


class ProvinceFilter(FilterSet):
    region = NumberFilter()
    number_plates = NumberFilter()
    neighbours = NumberFilter()
    districts_count = NumberFilter()
    districts_count__gt = NumberFilter(field_name='districts_count', lookup_expr='gt')
    districts_count__lt = NumberFilter(field_name='districts_count', lookup_expr='lt')
    wards_count = NumberFilter()
    wards_count__gt = NumberFilter(field_name='wards_count', lookup_expr='gt')
    wards_count__lt = NumberFilter(field_name='wards_count', lookup_expr='lt')    
    is_border = BooleanFilter()
    is_coastal = BooleanFilter()

    class Meta:
        model = Province
        fields = {
            'area': ['gt', 'lt'],    
            'population': ['gt', 'lt'],
        }

    