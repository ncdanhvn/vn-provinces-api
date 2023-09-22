from rest_framework import serializers
from .models import Region, Province, District, Ward


# Model serializers
model_fields = ['name', 'name_en', 'id', 'type']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'name_en', 'id']


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = model_fields


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = model_fields


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = model_fields


# Basic serializers (for views with 'basic' parameter)
# Basic serializers = model serializers + upper_level_model_id
class ProvinceBasicSerializer(ProvinceSerializer):
    class Meta(ProvinceSerializer.Meta):
        fields = ProvinceSerializer.Meta.fields + ['region_id']


class DistrictBasicSerializer(DistrictSerializer):
    class Meta(DistrictSerializer.Meta):
        fields = DistrictSerializer.Meta.fields + ['province_id']


class WardBasicSerializer(WardSerializer):
    class Meta(WardSerializer.Meta):
        fields = WardSerializer.Meta.fields + ['district_id', 'province_id']

    province_id = serializers.IntegerField(source='district.province.id')


# List and Details serializers
class RegionListSerializer(RegionSerializer):
    class Meta(RegionSerializer.Meta):
        fields = RegionSerializer.Meta.fields + ['provinces_count']

    provinces_count = serializers.IntegerField()


class RegionDetailsSerializer(RegionListSerializer):
    class Meta(RegionListSerializer.Meta):
        fields = RegionListSerializer.Meta.fields + ['provinces']

    provinces = ProvinceSerializer(many=True)


class ProvinceListSerializer(ProvinceSerializer):
    class Meta(ProvinceSerializer.Meta):
        fields = ProvinceSerializer.Meta.fields + ['region', 'area', 'population',
                                                   'number_plates', 'is_border', 'is_coastal', 'neighbours', 'districts_count', 'wards_count']

    region = RegionSerializer()
    is_border = serializers.BooleanField()
    is_coastal = serializers.BooleanField()
    neighbours = ProvinceSerializer(many=True)
    districts_count = serializers.IntegerField()
    wards_count = serializers.IntegerField()


class ProvinceDetailsSerializer(ProvinceListSerializer):
    class Meta(ProvinceListSerializer.Meta):
        fields = ProvinceListSerializer.Meta.fields + ['districts']

    districts = DistrictSerializer(many=True)


class DistrictListSerializer(DistrictSerializer):
    class Meta(DistrictSerializer.Meta):
        fields = DistrictSerializer.Meta.fields + \
            ['province', 'is_border', 'is_coastal', 'wards_count']

    wards_count = serializers.IntegerField()
    province = ProvinceBasicSerializer()


class DistrictDetailsSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = DistrictListSerializer.Meta.fields + ['wards']

    wards = WardSerializer(many=True)


class WardListSerializer(WardSerializer):
    class Meta(WardSerializer.Meta):
        fields = WardSerializer.Meta.fields + ['district', 'province']

    district = DistrictSerializer()
    province = ProvinceBasicSerializer(source='district.province')