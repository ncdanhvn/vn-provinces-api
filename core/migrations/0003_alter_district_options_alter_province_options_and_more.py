# Generated by Django 4.2 on 2023-05-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_region_alter_province_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ward',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='district',
            name='type',
            field=models.CharField(choices=[('C', 'City'), ('UD', 'Urban District'), ('RD', 'Rural District'), ('T', 'Town')], default='UD', max_length=2),
        ),
    ]
