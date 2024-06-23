from django.db import models

class Klients (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

