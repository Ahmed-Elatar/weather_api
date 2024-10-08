# Generated by Django 5.0.8 on 2024-08-09 03:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCurrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField()),
                ('temp_c', models.FloatField()),
                ('wind_kph', models.FloatField()),
                ('wind_dir', models.CharField(max_length=10)),
                ('pressure_mb', models.FloatField()),
                ('cloud', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('tz_id', models.CharField(max_length=255)),
                ('localtime_epoch', models.IntegerField()),
                ('localtime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.weathercurrent')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.weatherlocation')),
            ],
        ),
    ]
