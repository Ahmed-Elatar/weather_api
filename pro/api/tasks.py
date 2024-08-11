from celery import shared_task
from . import views
from time import sleep
from .serializers import *


@shared_task
def try_1():
    for i in range(1,11):
        print(i)
        sleep(0.5)
    return "DONE"
    


@shared_task
def try_2():
    Data=views.get_weather()
    serializer = WeatherDataSerializer(data=Data)
    if serializer.is_valid():
        serializer.save()
