from django.db.models import Count, Max, Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import logging
from .models import Region, Province, District, Ward
from .serializers import *
from .pagination import *
from .filters import *
from .docs.extend_schemas import *


logger = logging.getLogger(__name__)


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.prefetch_related('provinces') \
        .annotate(provinces_count=Count('provinces'))

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializer
        if self.action == 'retrieve':
            return RegionDetailsSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['id']

    # For documentation generation
    @regions_list_extend_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @region_details_extend_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProvinceViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        basic = self.request.query_params.get('basic')
        if basic and (self.action == 'list'):
            self.filterset_class = BasicProvinceFilter 
            return Province.objects.only('name', 'type', 'region_id')

        # Not basic
        self.filterset_class = ProvinceFilter

        if self.action == 'list':
            return Province.objects \
                .select_related('region') \
                .prefetch_related('number_plates') \
                .prefetch_related('neighbours') \
                .prefetch_related('districts') \
                .annotate(
                    districts_count=Count('districts', distinct=True),
                    wards_count=Count('districts__wards'),
                    is_border=Max('districts__is_border'),
                    is_coastal=Max('districts__is_coastal'))

        if self.action == 'retrieve':
            return Province.objects \
                .select_related('region') \
                .prefetch_related('number_plates') \
                .prefetch_related('neighbours') \
                .prefetch_related('districts__wards') \
                .annotate(
                    districts_count=Count('districts', distinct=True),
                    wards_count=Count('districts__wards'),
                    is_border=Max('districts__is_border'),
                    is_coastal=Max('districts__is_coastal'))

    def get_serializer_class(self):
        basic = self.request.query_params.get('basic')
        if basic and (self.action == 'list'):
            return ProvinceBasicSerializer

        return ProvinceListSerializer if self.action == 'list' else ProvinceDetailsSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']
    pagination_class = DefaultPagination

    # For documentation generation
    @provinces_list_extend_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @province_details_extend_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DistrictViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        basic = self.request.query_params.get('basic')
        if basic and (self.action == 'list'):
            self.filterset_class = BasicDistrictFilter 
            return District.objects.only('name', 'type', 'province_id')

        # Not basic
        self.filterset_class = DistrictFilter

        return District.objects \
            .select_related('province') \
            .prefetch_related('wards') \
            .annotate(wards_count=Count('wards'))

    def get_serializer_class(self):
        basic = self.request.query_params.get('basic')
        if basic and (self.action == 'list'):           
            return DistrictBasicSerializer

        return DistrictListSerializer if self.action == 'list' else DistrictDetailsSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']
    pagination_class = DefaultPagination

    # For documentation generation
    @districts_list_extend_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @district_details_extend_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class WardViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        basic = self.request.query_params.get('basic')
        if basic and (self.action == 'list'):
            return Ward.objects \
                .select_related('district', 'district__province') \
                .only('name', 'type', 'district_id', 'district__province__id')

        return Ward.objects.select_related('district', 'district__province')

    def get_serializer_class(self):
        basic = self.request.query_params.get('basic')
        return WardBasicSerializer if basic and self.action =='list' else WardListSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WardFilter
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']
    pagination_class = DefaultPagination

    # For documentation generation
    @wards_list_extend_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @ward_details_extend_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class WardFromAProvinceViewSet(ListModelMixin, GenericViewSet):
    def get_queryset(self):
        queryset = Ward.objects.filter(
            district__province__id=self.kwargs['province_pk'])

        basic = self.request.query_params.get('basic')
        if basic:
            return queryset \
                .select_related('district', 'district__province') \
                .only('name', 'type', 'district_id', 'district__province__id')

        return queryset.select_related('district', 'district__province')

    def get_serializer_class(self):
        basic = self.request.query_params.get('basic')        
        return WardBasicSerializer if basic else WardListSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = WardFilter
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']
    pagination_class = DefaultPagination

    # For documentation generation
    @wards_nested_list_extend_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
