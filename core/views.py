from django.db.models import Count, Max, Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Region, Province, District, Ward
from .serializers import RegionListSerializer, RegionDetailsSerializer, ProvinceListSerializer, ProvinceDetailsSerializer, DistrictListSerializer, DistrictDetailsSerializer, WardSerializer, WardNoProvinceSerializer, ProvinceShortSerializer, ProvinceDetailsShortSerializer
from .pagination import DefaultPagination, NameOnlyPagination
from .filters import ProvinceFilter, DistrictFilter, WardFilter


class RegionViewSet(ReadOnlyModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Region.objects.prefetch_related('provinces') \
                    .annotate(provinces_count=Count('provinces'))
        if self.action == 'retrieve':
            province_prefetch = Prefetch('provinces', 
                                         queryset=Province.objects \
                                            .select_related('region') \
                                            .prefetch_related('number_plates') \
                                            .prefetch_related('neighbours') \
                                            .prefetch_related('districts') \
                                            .annotate(
                                                districts_count=Count('districts', distinct=True), 
                                                wards_count=Count('districts__wards'),
                                                is_border=Max('districts__is_border'),
                                                is_coastal=Max('districts__is_coastal')))
            return Region.objects.prefetch_related(province_prefetch) \
                    .annotate(provinces_count=Count('provinces'))

    def get_serializer_class(self):
        if self.action == 'list':
            return RegionListSerializer
        if self.action == 'retrieve':
            return RegionDetailsSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['id']


class ProvinceViewSet(ReadOnlyModelViewSet):                 
    def get_queryset(self):
        name_only = self.request.query_params.get('name_only')

        if name_only:
            self.pagination_class = NameOnlyPagination
            self.filter_backends = [SearchFilter, OrderingFilter]  
            return Province.objects.only('name')

        # Not name_only
        self.filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]   
        self.pagination_class = DefaultPagination   
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
        name_only = self.request.query_params.get('name_only')
        if name_only:
            if self.action == 'list':
                return ProvinceShortSerializer
            return ProvinceDetailsShortSerializer
                
        if self.action == 'list':
            return ProvinceListSerializer
        if self.action == 'retrieve':
            return ProvinceDetailsSerializer

    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']


class DistrictViewSet(ReadOnlyModelViewSet):
    queryset = District.objects \
                .select_related('province') \
                .prefetch_related('wards') \
                .annotate(wards_count=Count('wards'))

    def get_serializer_class(self):
        if self.action == 'list':
            return DistrictListSerializer
        if self.action == 'retrieve':
            return DistrictDetailsSerializer
        
    pagination_class = DefaultPagination 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DistrictFilter   
    search_fields = ['name']    
    ordering_fields = '__all__' 
    ordering = ['name']


class WardViewSet(ReadOnlyModelViewSet):
    queryset = Ward.objects.select_related('district', 'district__province')
    serializer_class = WardSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = WardFilter 
    search_fields = ['name']     
    ordering_fields = '__all__'
    ordering = ['name']


class WardFromAProvinceViewSet(ReadOnlyModelViewSet):   
    def get_queryset(self):        
        return Ward.objects \
                .filter(district__province__id=self.kwargs['province_pk']) \
                .select_related('district')
    
    serializer_class = WardNoProvinceSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = WardFilter         
    search_fields = ['name']
    ordering_fields = '__all__'
    ordering = ['name']
