from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,JsonResponse
from rest_framework import  status , viewsets ,generics 
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,ListCreateAPIView
from rest_framework.response import Response
from .forms import *
from .models import *
from .serializers import *
from .tasks import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import requests
import json
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination

# Create your views here.











"""
Fetch and process current weather data for a specific location.

This function retrieves the current weather data for a given location using the WeatherAPI
and uses nested_to_flastten() function to flattens nested JSON data into a single dictionary. 
It also extracts and reformats the date and time from the weather data.

Parameters:
    loc (str): The location for which to fetch weather data. 
                Example: 'Cairo'

Example:
    weather_data = get_weather('Alexandria')

Returns:
    dict: A dictionary containing flattened weather data with keys such as 'temp_c', 
            'humidity', 'wind_kph', 'pressure_mb', 'date', 'time', etc.

            Example:
            {
                "temp_c": 27.3,
                "humidity": 78,
                "wind_kph": 13.7,
                "pressure_mb": 1009.0,
                "date": datetime.date(2024, 8, 11),
                "time": datetime.time(2, 15),
                ...
            }


Notes:
    - The function uses an API-Token key to access the WeatherAPI service. Make sure your key is valid.

"""
def get_weather(loc):
    
    
    api_key='62a1c9aaf1294d17a5a232230240808'

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={loc}'
    # 'http://api.weatherapi.com/v1/current.json?key=62a1c9aaf1294d17a5a232230240808&q=Cairo'
    
    try :
        response = requests.get(url)
        data =response.json()
        
        
        
        flat_data=nested_to_flastten(data)


        
        dt= datetime.strptime(flat_data['last_updated'], "%Y-%m-%d %H:%M")

        flat_data['date'] = dt.date()
        flat_data['time'] = dt.time()
        flat_data.pop('localtime_epoch','localtime','last_updated')


        return flat_data 
    except :
        return  flat_data
    




"""
    
    This function flattens nested JSON data into a single dictionary.

    Parameters:
        nested_data ( dict(dict) ): The location for which to fetch weather data. 
                Example: 'nested_data'
                nested_data={
                                "location": {
                                    "name": "Austin",
                                    "region": "Texas",
                                    "country": "United States of America",
                                    "lat": 30.27,
                                    "lon": -97.74,
                                    "tz_id": "America/Chicago",
                                    "localtime_epoch": 1723631062,
                                    "localtime": "2024-08-14 05:24"
                                },
                                "current": {
                                    "last_updated": "2024-08-14 05:15",
                                    "temp_c": 26.7,
                                    "wind_kph": 6.8,
                                    "wind_dir": "S",
                                    "pressure_mb": 1017,
                                    "cloud": 25
                                }
                            }

    Example:
        weather_data = nested_to_flastten(nested_data)

    Returns:
        dict: A dictionary containing flattened weather data with keys such as 'temp_c', 
              'name', 'wind_kph', 'pressure_mb', 'date', 'time', etc.

              Example:
                      {
                        
                        "name": "Austin",
                        "region": "Texas",
                        "country": "United States of America",
                        "lat": 30.27,
                        "lon": -97.74,
                        "tz_id": "America/Chicago",
                        "date": "2024-08-13",
                        "time": "06:45:00",
                        "temp_c": 26.8,
                        "wind_kph": 10.4,
                        "wind_dir": "S",
                        "pressure_mb": 1015.0,
                        "cloud": 54
                    }


    
"""
def nested_to_flastten(nested_data):
    flat_data={}
    for key_outer, value_outer in nested_data.items():
        if isinstance(value_outer, dict):
            for key_inner, value_inner in value_outer.items():
                flat_data[key_inner] = value_inner
        else:
            flat_data[key_outer] = value_outer


    return flat_data







"""
WeatherListView class 
API view to retrieve a list of weather data or create a new record.


This view have 2 methods:

- GET : Returns a list of all weather data records .
- POST : Allows clients to create a new record in JSON format .

Attributes:
    queryset: A Django QuerySet that retrieves all WeatherData objects from the database.
    serializer_class: The serializer class which used to convert WeatherData instances to and from JSON.

"""
class WeatherListView(ListCreateAPIView):
    queryset =WeatherData.objects.all()
    serializer_class =WeatherDataSerializer



"""
    WeatherDetailView class 
    API view to retrieve a single record of weather data or update a record or delete a record.

    
    This view have 3 methods:

    - GET : Retrieves a specific weather data record by its primary key (ID).
    - PATCH : Partially or fully updates a specific weather data record.
    - DELETE : Deletes a specific weather data record.

    Attributes:
        queryset: A Django QuerySet that retrieves all WeatherData objects from the database.
        serializer_class: The serializer class which used to convert WeatherData instances to and from JSON.

    """
class WeatherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer



