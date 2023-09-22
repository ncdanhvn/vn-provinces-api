from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'name_en', 'id', 'type']


class ProvinceShortSerializer(ShortSerializer):
    class Meta(ShortSerializer.Meta):
        model = Province


class DistrictShortSerializer(ShortSerializer):
    class Meta(ShortSerializer.Meta):
        model = District


class WardShortSerializer(ShortSerializer):
    class Meta(ShortSerializer.Meta):
        model = Ward


class WardNoProvinceSerializer(WardShortSerializer):
    class Meta(WardShortSerializer.Meta):
        fields = WardShortSerializer.Meta.fields + ['district']

    district = DistrictShortSerializer()


class WardSerializer(WardNoProvinceSerializer):
    class Meta(WardNoProvinceSerializer.Meta):
        fields = WardNoProvinceSerializer.Meta.fields + ['province']

    province = ProvinceShortSerializer(source='district.province')


class DistrictListSerializer(DistrictShortSerializer):
    class Meta(DistrictShortSerializer.Meta):
        fields = DistrictShortSerializer.Meta.fields + ['province', 'is_border', 'is_coastal', 'wards_count']

    wards_count = serializers.IntegerField()
    province = ProvinceShortSerializer()


class DistrictDetailsSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = DistrictListSerializer.Meta.fields + ['wards']

    wards = WardShortSerializer(many=True)


class DistrictListNoProvinceSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = [field for field in DistrictListSerializer.Meta.fields
                  if field != 'province']

    wards_count = serializers.IntegerField(source='wards.count')


class RegionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'name_en', 'id']


class ProvinceListSerializer(ProvinceShortSerializer):
    class Meta(ProvinceShortSerializer.Meta):
        fields = ProvinceShortSerializer.Meta.fields + ['region', 'area', 'population',
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
