from rest_framework import serializers
from .models import Region, Province, District, Ward


class WardShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name']


class DistrictShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'type']


class ProvinceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'type']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'type', 'district']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'type', 'province']

    province = ProvinceShortSerializer()


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'type', 'region', 'districts']

    districts = DistrictShortSerializer(many=True)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'provinces']

    provinces = ProvinceShortSerializer(many=True)
