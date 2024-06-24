from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'country']

class RestaurantRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'country', 'city']
