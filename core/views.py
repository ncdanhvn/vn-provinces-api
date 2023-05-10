from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Region, Province, District, Ward
from .serializers import RegionListSerializer, RegionDetailsSerializer, ProvinceListSerializer, ProvinceDetailsSerializer, DistrictListSerializer, DistrictDetailsSerializer, WardSerializer
from .pagination import DefaultPagination
from django.http import HttpResponse
import csv


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


# def say_hello(request):
#     # add_coastal_districts()
#     print(District.objects.filter(is_coastal=True).count())
#     return HttpResponse('Hello World')


# def add_border_districts():
#     # Read data from border_districts.csv
#     found_count = 0
#     with open('core/data/border_districts.csv', newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for row in reader:
#             province_name = row[0]
#             district_name = row[1]

#             # Find province and district with the same name
#             try:
#                 province = Province.objects.filter(name=province_name).first()
#                 district = District.objects.filter(province__id=province.id, name=district_name).first()
#                 if district and province:
#                     district.is_border=True
#                     district.save()
#                     found_count += 1
#                 else:
#                     print('Error when finding district ', province_name, district_name)
#             except:
#                 print('Error when finding district ', province_name, district_name)
#     print(found_count)
        

# def add_coastal_districts():
#     # Read data from coastal_districts.csv
#     found_count = 0
#     with open('core/data/coastal_districts.csv', newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for row in reader:
#             province_name = row[0]
#             district_name = row[1]

#             # Find province and district with the same name
#             try:
#                 province = Province.objects.filter(name=province_name).first()
#                 district = District.objects.filter(province__id=province.id, name=district_name).first()
#                 if district and province:
#                     district.is_coastal=True
#                     district.save()
#                     found_count += 1
#                 else:
#                     print('Error when finding district ', province_name, district_name)
#             except:
#                 print('Error when finding district ', province_name, district_name)
#     print(found_count)
        
