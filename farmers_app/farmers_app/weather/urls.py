from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_home, name='weather_home'),
]
