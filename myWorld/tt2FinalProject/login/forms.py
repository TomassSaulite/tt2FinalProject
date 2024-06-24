from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    lastName = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50, required=True)
    country = forms.CharField(max_length=3, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name', 'lastName','email','country',)
