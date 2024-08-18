from celery import shared_task
from . import views
from time import sleep
from .serializers import *


cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", 
    "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", 
    "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", 
    "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis", "Louisville", 
    "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", 
    "Kansas City", "Mesa", "Atlanta", "Omaha", "Colorado Springs", "Raleigh", 
    "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", 
    "Tulsa", "Arlington", "Tampa", "New Orleans", "Wichita", "Cleveland", 
    "Bakersfield", "Aurora", "Anaheim", "Honolulu", "Santa Ana", "Riverside", 
    "Corpus Christi", "Lexington", "Henderson", "Stockton", "St. Louis", 
    "Saint Paul", "Cincinnati", "Pittsburgh", "Greensboro", "Anchorage", 
    "Plano", "Lincoln", "Orlando", "Irvine", "Newark", "Toledo", "Durham", 
    "Chula Vista", "Fort Wayne", "Jersey City", "St. Petersburg", "Laredo", 
    "Madison", "Chandler", "Buffalo", "Lubbock", "Scottsdale", "Reno", 
    "Glendale", "Gilbert", "Winston-Salem", "North Las Vegas", "Norfolk", 
    "Chesapeake", "Garland", "Irving", "Hialeah", "Fremont", "Boise", 
    "Richmond", "Baton Rouge", "Spokane", "Des Moines", "Tacoma"
]








"""
get_cities_weather Background Task

This Celery task call get_weather() function from views and send the parameter ( city name ) to get city weather data
The function uses a global counter (`cnt`) to keep track of which cities have been processed 
note :
    - he task processes 10 cities per run ( from the cities list )
    
Then save the data returned from  get_weather() in database using  WeatherDataSerializer



Parameters:
    None

Returns:
    None

"""
cnt=0
@shared_task
def get_cities_weather():
    global cnt
    
    for i in range(10):
        if cnt > len(cities)-1 :
            cnt=0
        
        Data = views.get_weather(cities[cnt])
        serializer = WeatherDataSerializer(data=Data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['name'])
        
        cnt+=1
    
