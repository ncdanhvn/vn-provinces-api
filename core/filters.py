from django_filters import NumberFilter, BooleanFilter
from django_filters.rest_framework import FilterSet
from .models import Province, District, Ward


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
            'type': ['exact'],
            'area': ['gt', 'lt'],    
            'population': ['gt', 'lt'],
        }


class BasicProvinceFilter(FilterSet):
    class Meta:
        model = Province
        fields = {
            'type': ['exact'],
        }


class DistrictFilter(FilterSet):
    province_id = NumberFilter(field_name='province_id')
    is_border = BooleanFilter()
    is_coastal = BooleanFilter()
    wards_count = NumberFilter()
    wards_count__gt = NumberFilter(field_name='wards_count', lookup_expr='gt')
    wards_count__lt = NumberFilter(field_name='wards_count', lookup_expr='lt')    

    class Meta:
        model = District
        fields = {'type': ['exact']}


class BasicDistrictFilter(FilterSet):
    province_id = NumberFilter(field_name='province_id')

    class Meta:
        model = District
        fields = {
            'type': ['exact'],
        }


class WardFilter(FilterSet):
    province_id = NumberFilter(field_name='district__province__id')
    district_id = NumberFilter(field_name='district_id')

    class Meta:
        model = Ward
        fields = {'type': ['exact']}
