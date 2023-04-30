from django.db import models


class Province(models.Model):
    TYPE_CITY = 'C'         # Thành Phố trực thuộc TW
    TYPE_PROVINCE = 'P'     # Tỉnh

    TYPE_CHOICES = [
        (TYPE_CITY, 'City'),
        (TYPE_PROVINCE, 'Province')
    ]

    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_PROVINCE)


class District(models.Model):
    TYPE_CITY = 'C'         # City - Thành phố trực thuộc tỉnh/thành phố
    TYPE_DISTRICT = 'D'     # District - Quận hoặc Huyện
    TYPE_TOWN = 'T'         # Town - Thị xã

    TYPE_CHOICES = [
        (TYPE_CITY, 'City'),
        (TYPE_DISTRICT, 'District'),
        (TYPE_TOWN, 'Town')
    ]

    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, related_name='districts')
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_DISTRICT)


class Ward(models.Model):
    TYPE_WARD = 'W'         # Ward - Phường
    TYPE_COMMUNE = 'C'      # Commune - Xã

    TYPE_CHOICES = [
        (TYPE_WARD, 'Ward'),
        (TYPE_COMMUNE, 'Commune')
    ]

    name = models.CharField(max_length=255)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, related_name='wards')
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_WARD)