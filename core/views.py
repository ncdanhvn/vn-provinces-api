from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region, Province, District, Ward
from .serializers import RegionListSerializer, RegionDetailsSerializer, ProvinceListSerializer, ProvinceDetailsSerializer, DistrictListSerializer, DistrictDetailsSerializer, WardSerializer
from .pagination import DefaultPagination


class RegionViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Region.objects.prefetch_related('provinces')
        if self.action == 'retrieve':
            return Region.objects.prefetch_related('provinces', 'provinces__districts')

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializer
        if self.action == 'retrieve':
            return RegionDetailsSerializer


class ProvinceViewSet(ReadOnlyModelViewSet): 
    pagination_class = DefaultPagination   

    def get_queryset(self):
        if self.action == 'list':
            return Province.objects \
                    .select_related('region') \
                    .prefetch_related('number_plates') \
                    .prefetch_related('neighbours') \
                    .annotate(districts_count=Count('districts', distinct=True), wards_count=Count('districts__wards')) 
        if self.action == 'retrieve':
            return Province.objects \
                    .select_related('region') \
                    .prefetch_related('number_plates') \
                    .prefetch_related('neighbours') \
                    .prefetch_related('districts__wards') \
                    .annotate(districts_count=Count('districts', distinct=True), wards_count=Count('districts__wards'))         

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
    queryset = Ward.objects.select_related('district', 'district__province')
    serializer_class = WardSerializer
    pagination_class = DefaultPagination
