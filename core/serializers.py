from rest_framework import serializers
from .models import Region, Province, District, Ward
from .utils.vn_to_en import remove_accents


class ProvinceShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en']


class DistrictShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'name_en']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'district', 'province']

    type = serializers.SerializerMethodField(method_name='get_ward_type')
    type_en = serializers.SerializerMethodField(method_name='get_ward_en_type')
    district = DistrictShortSerializer()
    province = ProvinceShortSerializer(source='district.province')

    def get_ward_type(self, ward):
        return get_type(ward)
        
    def get_ward_en_type(self, ward):
        return get_type(ward, en=True)


class WardNoDistrictSerializer(WardSerializer):
    class Meta(WardSerializer.Meta):
        fields = ['id', 'name', 'name_en', 'type', 'type_en']


class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 
                  'province', 'is_border', 'is_coastal' ,'wards_count', ]
    
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
        fields = DistrictListSerializer.Meta.fields + ['wards']

    wards = WardNoDistrictSerializer(many=True)


class DistrictListNoProvinceSerializer(DistrictListSerializer):
    class Meta(DistrictListSerializer.Meta):
        fields = [field for field in DistrictListSerializer.Meta.fields 
                  if field not in['province']]


class RegionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'name_en']

    
class ProvinceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en', 'type', 'type_en', 'region', 'area', 'population', 
                  'number_plates', 'is_border', 'is_coastal', 'neighbours', 'districts_count', 'wards_count']
    
    type = serializers.SerializerMethodField(method_name='get_province_type')
    type_en = serializers.SerializerMethodField(method_name='get_province_type_en')
    region = RegionShortSerializer()
    is_border = serializers.SerializerMethodField()
    is_coastal = serializers.SerializerMethodField()
    neighbours = ProvinceShortSerializer(many=True)
    districts_count = serializers.IntegerField()
    wards_count = serializers.IntegerField()
    
    def get_is_border(self, province: Province):
        for district in province.districts.all():
            if district.is_border:
                return True
        return False
    
    def get_is_coastal(self, province: Province):
        for district in province.districts.all():
            if district.is_coastal:
                return True
        return False

    def get_province_type(self, province):
        return get_type(province)
    
    def get_province_type_en(self, province):
        return get_type(province, en=True)
    

class ProvinceDetailsSerializer(ProvinceListSerializer):
    class Meta(ProvinceListSerializer.Meta):
        fields = ProvinceListSerializer.Meta.fields + ['districts']

    districts = DistrictListNoProvinceSerializer(many=True)


class ProvinceListNoRegionSerializer(ProvinceListSerializer):
    class Meta(ProvinceListSerializer.Meta):
        fields = [field for field in ProvinceListSerializer.Meta.fields 
                  if field not in['region', 'districts_count', 'wards_count']]


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'name_en', 'provinces_count']

    provinces_count = serializers.IntegerField(source='provinces.count')


class RegionDetailsSerializer(RegionListSerializer):
    class Meta(RegionListSerializer.Meta):
        fields = RegionListSerializer.Meta.fields + ['provinces']

    provinces = ProvinceListNoRegionSerializer(many=True)


def get_type(object, en=False):
    if en:
        ts = [item for item in object.TYPE_EN_CHOICES if item[0] == object.type]
    else:
        ts = [item for item in object.TYPE_CHOICES if item[0] == object.type]
    return ts[0][1]
