from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region, Province, District, Ward
from .serializers import RegionListSerializer, RegionDetailsSerializer, ProvinceListSerializer, ProvinceDetailsSerializer, DistrictSerializer, WardSerializer
from .pagination import DefaultPagination


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.prefetch_related('provinces')

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializer
        if self.action == 'retrieve':
            return RegionDetailsSerializer


class ProvinceViewSet(ReadOnlyModelViewSet):
    queryset = Province.objects.prefetch_related(
        'districts').select_related('region')    
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ProvinceListSerializer
        if self.action == 'retrieve':
            return ProvinceDetailsSerializer


class DistrictViewSet(ReadOnlyModelViewSet):
    queryset = District.objects.select_related('province')
    serializer_class = DistrictSerializer
    pagination_class = DefaultPagination


class WardViewSet(ReadOnlyModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    pagination_class = DefaultPagination
