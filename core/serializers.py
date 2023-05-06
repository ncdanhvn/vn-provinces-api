from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class WardShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'type']

    type = serializers.SerializerMethodField(method_name='get_ward_type')

    def get_ward_type(self, ward):
        return get_type(ward)


class DistrictShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'type']

    type = serializers.SerializerMethodField(method_name='get_district_type')

    def get_district_type(self, district):
        return get_type(district)
    

class ProvinceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'type']

    type = serializers.SerializerMethodField(method_name='get_province_type')

    def get_province_type(self, province):
        return get_type(province)
    

class RegionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'type', 'district']

    type = serializers.SerializerMethodField(method_name='get_ward_type')

    def get_ward_type(self, ward):
        return get_type(ward)
    

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'type', 'province']

    province = ProvinceShortSerializer()
    type = serializers.SerializerMethodField(method_name='get_district_type')

    def get_district_type(self, district):
        return get_type(district)


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en', 'type', 'type_en','region', 'districts']

    districts = DistrictShortSerializer(many=True)
    name_en = serializers.SerializerMethodField(method_name='get_name_en')
    type = serializers.SerializerMethodField(method_name='get_province_type')
    type_en = serializers.SerializerMethodField(method_name='get_province_type_en')
    region = RegionShortSerializer()
    
    def get_province_type(self, province):
        return get_type(province)
    
    def get_name_en(self, province):
        return remove_accents(province.name)
    
    def get_province_type_en(self, province):
        return get_type(province, en=True)
    

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'name_en', 'provinces']

    provinces = ProvinceShortSerializer(many=True)


def get_type(object, en=False):
    if en:
        ts = [item for item in object.TYPE_EN_CHOICES if item[0] == object.type]
    else:
        ts = [item for item in object.TYPE_CHOICES if item[0] == object.type]
    return ts[0][1]
