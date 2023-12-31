# Generated by Django 4.2.1 on 2023-05-08 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_province_area_province_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='number_plates', to='core.province')),
            ],
        ),
    ]
