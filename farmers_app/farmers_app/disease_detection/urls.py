from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_disease, name='detect_disease'),
]
