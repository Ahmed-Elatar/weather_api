from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

from .resource import WeatherResource 


# Register your models here.

@admin.register(WeatherData)
class WeatherAdmin(ImportExportModelAdmin):
    resource_class = WeatherResource
    list_display =['name','date','time', 'tz_id','temp_c','wind_dir','pressure_mb']      






