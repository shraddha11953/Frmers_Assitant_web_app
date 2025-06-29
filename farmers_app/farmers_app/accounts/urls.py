from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home', views.home, name='home'),
    path('',views.index, name='index'),
    path('signup/farmer/', views.farmer_signup, name='farmer_signup'),
    path('signup/buyer/', views.buyer_signup, name='buyer_signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
