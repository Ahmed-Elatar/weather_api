from rest_framework import serializers
from .models import *



# class WeatherCurrentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =WeatherCurrent
#         fields = '__all__'


# class WeatherLocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =WeatherLocation
#         fields = '__all__'


# class WeatherSerializer(serializers.ModelSerializer):
#     location = WeatherLocationSerializer()
#     current = WeatherCurrentSerializer()
    
#     class Meta:
#         model =Weather
#         fields = ['location' ,'current']





class WeatherDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =WeatherData
        fields = '__all__'
