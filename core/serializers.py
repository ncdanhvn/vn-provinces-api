from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class ProvinceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name', 'name_en', 'id']


class DistrictShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'name_en', 'id']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name', 'name_en', 'id', 'type', 'district', 'province']

    district = DistrictShortSerializer()
    province = ProvinceShortSerializer(source='district.province')


class WardNoDistrictSerializer(WardSerializer):
    class Meta(WardSerializer.Meta):
        fields = [field for field in WardSerializer.Meta.fields if field not in ['district', 'province']]


class WardNoProvinceSerializer(WardSerializer):
    class Meta(WardSerializer.Meta):
        fields = [field for field in WardSerializer.Meta.fields if field not in ['province']]


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'name_en', 'id', 'type',  
                  'province', 'is_border', 'is_coastal' ,'wards_count']
    
    wards_count = serializers.IntegerField()
    province = ProvinceShortSerializer()


class DistrictDetailsSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = DistrictListSerializer.Meta.fields + ['wards']

    wards = WardNoDistrictSerializer(many=True)


class DistrictListNoProvinceSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = [field for field in DistrictListSerializer.Meta.fields 
                  if field not in['province']]

    wards_count = serializers.IntegerField(source='wards.count')


class RegionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'name_en', 'id']

    
class ProvinceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name', 'name_en', 'id', 'type', 'region', 'area', 'population', 
                  'number_plates', 'is_border', 'is_coastal', 'neighbours', 'districts_count', 'wards_count']
    
    region = RegionShortSerializer()
    is_border = serializers.BooleanField()
    is_coastal = serializers.BooleanField()
    neighbours = ProvinceShortSerializer(many=True)
    districts_count = serializers.IntegerField()
    wards_count = serializers.IntegerField()


class ProvinceDetailsSerializer(ProvinceListSerializer):
    class Meta(ProvinceListSerializer.Meta):
        fields = ProvinceListSerializer.Meta.fields + ['districts']

    districts = DistrictListNoProvinceSerializer(many=True)


# class ProvinceListNoRegionSerializer(ProvinceListSerializer):
#     class Meta(ProvinceListSerializer.Meta):
#         fields = [field for field in ProvinceListSerializer.Meta.fields 
#                   if field not in['region']]


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'name_en', 'id', 'provinces_count']

    provinces_count = serializers.IntegerField()


class RegionDetailsSerializer(RegionListSerializer):
    class Meta(RegionListSerializer.Meta):
        fields = RegionListSerializer.Meta.fields + ['provinces']

    provinces = ProvinceShortSerializer(many=True)