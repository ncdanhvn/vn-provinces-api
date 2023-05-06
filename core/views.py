from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region, Province, District, Ward
from .serializers import RegionListSerializer, RegionDetailsSerializer, ProvinceListSerializer, ProvinceDetailsSerializer, DistrictListSerializer, DistrictDetailsSerializer, WardSerializer
from .pagination import DefaultPagination


class RegionViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Region.objects.prefetch_related('provinces')
        if self.action == 'retrieve':
            return Region.objects.prefetch_related(Prefetch(
                'provinces', 
                queryset=Province.objects.prefetch_related('districts')))

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializer
        if self.action == 'retrieve':
            return RegionDetailsSerializer


class ProvinceViewSet(ReadOnlyModelViewSet): 
    pagination_class = DefaultPagination

    def get_queryset(self):
        if self.action == 'list':
            return Province.objects.select_related('region').prefetch_related('districts')
        if self.action == 'retrieve':
            return Province.objects.select_related('region').prefetch_related(Prefetch(
                'districts', 
                queryset=District.objects.prefetch_related('wards')))  

    def get_serializer_class(self):
        if self.action == 'list':
            return ProvinceListSerializer
        if self.action == 'retrieve':
            return ProvinceDetailsSerializer


class DistrictViewSet(ReadOnlyModelViewSet):
    queryset = District.objects.select_related('province').prefetch_related('wards')
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return DistrictListSerializer
        if self.action == 'retrieve':
            return DistrictDetailsSerializer
        

class WardViewSet(ReadOnlyModelViewSet):
    queryset = Ward.objects.select_related('district')
    serializer_class = WardSerializer
    pagination_class = DefaultPagination
