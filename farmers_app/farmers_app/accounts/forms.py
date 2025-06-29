from django import forms
from .models import CustomUser, FarmerProfile, BuyerProfile
from django.contrib.auth.forms import UserCreationForm

class FarmerSignUpForm(UserCreationForm):
    location = forms.CharField()
    phone = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'farmer'
        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user,
                location=self.cleaned_data['location'],
                phone=self.cleaned_data['phone']
            )
        return user

class BuyerSignUpForm(UserCreationForm):
    phone = forms.CharField()
    preferences = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'buyer'
        if commit:
            user.save()
            BuyerProfile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                preferences=self.cleaned_data['preferences']
            )
        return user
