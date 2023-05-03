from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Province(models.Model):
    TYPE_CITY = 'C'         # Thành Phố trực thuộc TW
    TYPE_PROVINCE = 'P'     # Tỉnh

    TYPE_CHOICES = [
        (TYPE_CITY, 'City'),
        (TYPE_PROVINCE, 'Province')
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_PROVINCE)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='provinces')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class District(models.Model):
    TYPE_CITY = 'C'                 # City - Thành phố trực thuộc tỉnh/thành phố
    TYPE_URBAN_DISTRICT = 'UD'       # Urban District - Quận
    TYPE_RURAL_DISTRICT = 'RD'       # Rural District - Huyện
    TYPE_TOWN = 'T'                 # Town - Thị xã

    TYPE_CHOICES = [
        (TYPE_CITY, 'City'),
        (TYPE_URBAN_DISTRICT, 'Urban District'),
        (TYPE_RURAL_DISTRICT, 'Rural District'),
        (TYPE_TOWN, 'Town')
    ]

    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name='districts')
    type = models.CharField(
        max_length=2, choices=TYPE_CHOICES, default=TYPE_URBAN_DISTRICT)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Ward(models.Model):
    TYPE_WARD = 'W'         # Ward - Phường
    TYPE_COMMUNE = 'C'      # Commune - Xã
    TYPE_TOWN = "T"         # Town - Thị trấn

    TYPE_CHOICES = [
        (TYPE_WARD, 'Ward'),
        (TYPE_COMMUNE, 'Commune'),
        (TYPE_TOWN, 'Town'),
    ]

    name = models.CharField(max_length=255)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='wards')
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_WARD)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']