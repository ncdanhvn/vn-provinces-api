from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils.vn_to_en import remove_accents


class Region(models.Model):
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Province(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='provinces')
    area = models.DecimalField(max_digits=8, decimal_places=2)
    population = models.PositiveIntegerField()
    neighbours = models.ManyToManyField("self", symmetrical=True)
    
    # Province types
    TYPE_CITY = 'C'         # City - Thành Phố trực thuộc TW
    TYPE_PROVINCE = 'P'     # Province - Tỉnh

    TYPE_CHOICES = [
        (TYPE_CITY, 'City (Thành phố)'),
        (TYPE_PROVINCE, 'Province (Tỉnh)')
    ]

    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_PROVINCE)
    
    def name_en(self):
        return remove_accents(self.name)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class District(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name='districts')
    is_border = models.BooleanField(default=False)
    is_coastal = models.BooleanField(default=False)

    # District types
    TYPE_CITY = 'C'                 # City - Thành phố trực thuộc tỉnh/thành phố
    TYPE_URBAN_DISTRICT = 'UD'       # Urban District - Quận
    TYPE_RURAL_DISTRICT = 'RD'       # Rural District - Huyện
    TYPE_TOWN = 'T'                 # Town - Thị xã

    TYPE_CHOICES = [
        (TYPE_CITY, 'City (Thành phố)'),
        (TYPE_URBAN_DISTRICT, 'Urban District (Quận)'),
        (TYPE_RURAL_DISTRICT, 'Rural District (Huyện)'),
        (TYPE_TOWN, 'Town (Thị xã)')
    ]

    type = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=TYPE_URBAN_DISTRICT)

    def name_en(self):
        return remove_accents(self.name)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Ward(models.Model):  
    name = models.CharField(max_length=255)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='wards')
    
    # Ward types
    TYPE_WARD = 'W'         # Ward - Phường
    TYPE_COMMUNE = 'C'      # Commune - Xã
    TYPE_TOWN = "T"         # Town - Thị trấn
    
    TYPE_CHOICES = [
        (TYPE_WARD, 'Ward (Phường)'),
        (TYPE_COMMUNE, 'Commune (Xã)'),
        (TYPE_TOWN, 'Town (Thị trấn)'),
    ]

    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_WARD)
    
    def name_en(self):
        return remove_accents(self.name)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class NumberPlate(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT, related_name='number_plates')
    