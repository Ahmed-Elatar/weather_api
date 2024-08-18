from django.urls import path
from .views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi






schema_view = get_schema_view(
    openapi.Info(
        title="Weather - Api",
        default_version='v1',
    ),
)






urlpatterns = [

    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),




    path('', WeatherListView.as_view(), name='weather_list'),

    path('<int:pk>/', WeatherDetailView.as_view(), name='weather_detail'),


]
