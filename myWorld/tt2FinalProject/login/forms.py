from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        help_text=None,
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
        help_text=None,
    )
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50, required=True)
    country = forms.CharField(max_length=3, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name','email','country',)

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# from .models import CustomRestaurant
# class CustomRestaurantCreationForm(UserCreationForm):
#     name = forms.CharField(
#         label="Name",
#         help_text=None,
#     )
#     password1 = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput,
#         help_text=None,
#     )
#     password2 = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput,
#         strip=False,
#         help_text=None,
#     )
#     name = forms.CharField(max_length=50, required=True)
#     email = forms.CharField(max_length=50, required=True)
#     country = forms.CharField(max_length=3, required=True)
#     city = forms.CharField(max_length=50, required=True)
#     kitchen = forms.CharField(max_length=50, required=True)

#     class Meta(UserCreationForm.Meta):
#         model = CustomRestaurant
#         fields = UserCreationForm.Meta.fields + ('name','email','country','city','kitchen')