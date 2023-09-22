from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents

short_fields = ['name', 'name_en', 'id', 'type']


class ProvinceBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = short_fields


class DistrictBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = short_fields + ['province_id']


class WardBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = short_fields + ['district_id', 'province_id']

    province_id = serializers.IntegerField(source='district.province.id')


class DistrictNoProvinceBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = short_fields


class WardNoDistrictBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = short_fields


class WardNoProvinceBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields =short_fields + ['district_id']    


class ProvinceDetailsBasicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = short_fields + ['districts']
    
    districts = DistrictNoProvinceBasicSerializer(many=True)


class DistrictDetailsBasicSerializer(DistrictBasicSerializer):
    class Meta(DistrictBasicSerializer.Meta):
        fields = DistrictBasicSerializer.Meta.fields + ['wards']
    
    wards = WardNoDistrictBasicSerializer(many=True)