from typing import Any
from django.db import models

# Create your models here.


# class WeatherLocation(models.Model):
    
#     name = models.CharField(max_length=255)
#     region = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     lat = models.FloatField()
#     lon = models.FloatField()
#     tz_id = models.CharField(max_length=255)
#     localtime_epoch =models.IntegerField()
#     localtime =models.DateTimeField()

# class WeatherCurrent(models.Model):
#     last_updated = models.DateTimeField()
#     temp_c = models.FloatField()
#     wind_kph = models.FloatField()
#     wind_dir = models.CharField(max_length=10)
#     pressure_mb = models.FloatField()
#     cloud = models.IntegerField()


# class Weather(models.Model):
#     location = models.ForeignKey(WeatherLocation, on_delete=models.CASCADE)
#     current = models.OneToOneField(WeatherCurrent, on_delete=models.CASCADE)





class WeatherData(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    tz_id = models.CharField(max_length=255)
    # localtime_epoch = models.IntegerField()
    # localtime = models.DateTimeField()

    # last_updated = models.DateTimeField()
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    temp_c = models.FloatField()
    wind_kph = models.FloatField()
    wind_dir = models.CharField(max_length=10)
    pressure_mb = models.FloatField()
    cloud = models.IntegerField()

    def __str__(self):
        return f" {self.name} Weather at {self.date}"
