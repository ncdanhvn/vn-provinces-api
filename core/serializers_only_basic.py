from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'name_en', 'id', 'type']


class ProvinceBasicSerializer(BasicSerializer):
    class Meta(BasicSerializer.Meta):
        model = Province


class DistrictNoProvinceBasicSerializer(BasicSerializer):
    class Meta(BasicSerializer.Meta):
        model = District
        

class DistrictBasicSerializer(DistrictNoProvinceBasicSerializer):
    class Meta(DistrictNoProvinceBasicSerializer.Meta):
        fields = DistrictNoProvinceBasicSerializer.Meta.fields + ['province_id']


class WardNoDistrictBasicSerializer(BasicSerializer):
    class Meta(BasicSerializer.Meta):
        model = Ward


class WardNoProvinceBasicSerializer(WardNoDistrictBasicSerializer):
    class Meta(WardNoDistrictBasicSerializer.Meta):
        fields = WardNoDistrictBasicSerializer.Meta.fields + ['district_id']


class WardBasicSerializer(WardNoProvinceBasicSerializer):
    class Meta(WardNoProvinceBasicSerializer.Meta):
        fields = WardNoProvinceBasicSerializer.Meta.fields + ['province_id']

    province_id = serializers.IntegerField(source='district.province.id')


class ProvinceDetailsBasicSerializer(ProvinceBasicSerializer):
    class Meta(ProvinceBasicSerializer.Meta):
        fields = ProvinceBasicSerializer.Meta.fields + ['districts']

    districts = DistrictNoProvinceBasicSerializer(many=True)


class DistrictDetailsBasicSerializer(DistrictBasicSerializer):
    class Meta(DistrictBasicSerializer.Meta):
        fields = DistrictBasicSerializer.Meta.fields + ['wards']

    wards = WardNoDistrictBasicSerializer(many=True)
