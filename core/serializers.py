from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class DistrictShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'name_en']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'district']

    type = serializers.SerializerMethodField(method_name='get_ward_type')
    type_en = serializers.SerializerMethodField(method_name='get_ward_en_type')
    district = DistrictShortSerializer()

    def get_ward_type(self, ward):
        return get_type(ward)
        
    def get_ward_en_type(self, ward):
        return get_type(ward, en=True)


class ProvinceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en']
    

class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'wards_count', 'province']
    
    type = serializers.SerializerMethodField(method_name='get_district_type')
    type_en = serializers.SerializerMethodField(method_name='get_district_en_type')
    wards_count = serializers.IntegerField(source='wards.count')
    province = ProvinceShortSerializer()

    def get_district_type(self, district):
        return get_type(district)
    
    def get_district_en_type(self, district):
        return get_type(district, en=True)


class DistrictDetailsSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'province', 'wards_count', 'wards']

    wards = WardSerializer(many=True)


class RegionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'name_en']

    
class ProvinceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'districts_count', 'region']
    
    type = serializers.SerializerMethodField(method_name='get_province_type')
    type_en = serializers.SerializerMethodField(method_name='get_province_type_en')
    region = RegionShortSerializer()
    districts_count = serializers.IntegerField(source='districts.count')
    
    def get_province_type(self, province):
        return get_type(province)
    
    def get_province_type_en(self, province):
        return get_type(province, en=True)
    

class ProvinceDetailsSerializer(ProvinceListSerializer):
    class Meta(ProvinceListSerializer.Meta):
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'region', 'districts_count', 'districts']

    districts = DistrictListSerializer(many=True)


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'name_en', 'provinces_count']

    provinces_count = serializers.IntegerField(source='provinces.count')


class RegionDetailsSerializer(RegionListSerializer):
    class Meta(RegionListSerializer.Meta):
        fields = ['id', 'name', 'name_en', 'provinces_count', 'provinces']

    provinces = ProvinceListSerializer(many=True)


def get_type(object, en=False):
    if en:
        ts = [item for item in object.TYPE_EN_CHOICES if item[0] == object.type]
    else:
        ts = [item for item in object.TYPE_CHOICES if item[0] == object.type]
    return ts[0][1]
