from rest_framework import serializers
from .models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'provinces_count']

    provinces_count = serializers.IntegerField(read_only=True)
