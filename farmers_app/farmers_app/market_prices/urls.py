from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_prices_home, name='market_prices'),
]
