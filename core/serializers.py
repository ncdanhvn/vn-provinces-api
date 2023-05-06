from rest_framework import serializers
from .models import Region, Province, District, Ward


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
        fields = ['id', 'name', 'type', 'region', 'districts']

    districts = DistrictShortSerializer(many=True)
    type = serializers.SerializerMethodField(method_name='get_province_type')
    
    def get_province_type(self, province):
        return get_type(province)
    

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'provinces']

    provinces = ProvinceShortSerializer(many=True)


def get_type(object):
    ts = [item for item in object.TYPE_CHOICES if item[0] == object.type]
    return ts[0][1]