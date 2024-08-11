from django.urls import path
from .views import *




urlpatterns = [

    path('',index , name= "index"),
 
    path('weather/' , WeatherView.as_view(),name='view')
]
