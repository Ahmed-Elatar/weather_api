from import_export import resources 
from .models import *




class WeatherResource(resources.ModelResource):
    class Meta:
        model = WeatherData