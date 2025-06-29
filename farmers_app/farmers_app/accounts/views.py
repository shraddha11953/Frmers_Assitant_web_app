# Create your views here.
from django.shortcuts import render, redirect
from .forms import FarmerSignUpForm, BuyerSignUpForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

def home(request):
    return render(request, 'accounts/home.html')

def index(request):
    return render(request,'accounts/index.html')

def farmer_signup(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('marketplace')
    else:
        form = FarmerSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'user_type': 'Farmer'})

def buyer_signup(request):
    if request.method == 'POST':
        form = BuyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = BuyerSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'user_type': 'Buyer'})
