from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)

