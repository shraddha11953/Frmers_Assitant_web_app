# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = (
    ('farmer', 'Farmer'),
    ('buyer', 'Buyer'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class FarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    preferences = models.TextField(blank=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
