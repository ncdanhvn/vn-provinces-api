from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class ProvinceBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['name', 'name_en', 'id', 'type']


class DistrictBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'name_en', 'id', 'type', 'province_id']


class WardBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name', 'name_en', 'id', 'type', 'district_id', 'province_id']

    province_id = serializers.IntegerField(source='district.province.id')


class DistrictNoProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'name_en', 'id', 'type']


class WardNoDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name', 'name_en', 'id', 'type']  


class WardNoProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['name', 'name_en', 'id', 'type', 'district_id']    


class ProvinceDetailsBasicSerializer(ProvinceBasicSerializer):
    class Meta(ProvinceBasicSerializer.Meta):
        fields = ProvinceBasicSerializer.Meta.fields + ['districts']
    
    districts = DistrictNoProvinceSerializer(many=True)


class DistrictDetailsBasicSerializer(DistrictBasicSerializer):
    class Meta(DistrictBasicSerializer.Meta):
        fields = DistrictBasicSerializer.Meta.fields + ['wards']
    
    wards = WardNoDistrictSerializer(many=True)