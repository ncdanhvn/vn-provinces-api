# Generated by Django 4.2.1 on 2023-05-09 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_numberplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbouringProvince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='province_ones', to='core.province')),
                ('province_two', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='province_twos', to='core.province')),
            ],
            options={
                'unique_together': {('province_one', 'province_two')},
            },
        ),
    ]
