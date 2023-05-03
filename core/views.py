from django.db.models.aggregates import Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region, Province, District, Ward
from .serializers import RegionSerializer, ProvinceSerializer, DistrictSerializer, WardSerializer
from .pagination import DefaultPagination


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.prefetch_related(
        'provinces')
    serializer_class = RegionSerializer


class ProvinceViewSet(ReadOnlyModelViewSet):
    queryset = Province.objects.prefetch_related(
        'districts')
    serializer_class = ProvinceSerializer
    pagination_class = DefaultPagination


class DistrictViewSet(ReadOnlyModelViewSet):
    queryset = District.objects.select_related('province')
    serializer_class = DistrictSerializer
    pagination_class = DefaultPagination


class WardViewSet(ReadOnlyModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    pagination_class = DefaultPagination
