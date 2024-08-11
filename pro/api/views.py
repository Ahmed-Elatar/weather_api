from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
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


# Create your views here.




def index(request):
    try_1.delay()
    # print(request)
    x=get_weather()
    
    
    print(x)


    return HttpResponse("HOME.....")







def get_weather():
    
    loc='Alexandria'
    api_key='62a1c9aaf1294d17a5a232230240808'

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={loc}'
    #'http://api.weatherapi.com/v1/current.json?key={api_key}&q={loc}'  
    flat_data = {}

    try :
        response = requests.get(url)
        data =response.json()
        
        
        
        nested_data=data

        for key_outer, value_outer in nested_data.items():
            if isinstance(value_outer, dict):
                for key_inner, value_inner in value_outer.items():
                    flat_data[key_inner] = value_inner
            else:
                flat_data[key_outer] = value_outer

        
        dt= datetime.strptime(flat_data['last_updated'], "%Y-%m-%d %H:%M")

        flat_data['date'] = dt.date()
        flat_data['time'] = dt.time()
        flat_data.pop('localtime_epoch','localtime','last_updated')


        return flat_data 
    except :
        return  flat_data






class WeatherView(APIView):

    def get(self, request):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)