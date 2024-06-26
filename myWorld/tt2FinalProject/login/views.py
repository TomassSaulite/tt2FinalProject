from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# def updateLastAccess():
#   User = get_user_model()
#   user = User.objects.get(username=username)
#   user.last_login = datetime.datetime.now()
#   user.save()
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())


def regRest(request):
  template = loader.get_template('regRest.html')
  return HttpResponse(template.render())

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import CustomUserAuthenticationForm
from django.contrib.auth import get_user_model

import datetime
    
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            print(username)
            print(password)
            if user is not None:
                auth_login(request, user)
                # updateLastAccess()
                return redirect('index')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'login.html', {'form': form})
  
  
  
  
  


from .forms import RestaurantRegistrationForm

from django.contrib.auth.hashers import make_password

def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.set_password(request.POST['password'])
            restaurant.save()
            return redirect('index')
    else:
        form = RestaurantRegistrationForm()
    return render(request, 'registerRest.html', {'form': form})
  
  
  
  
  
  

from .forms import RestaurantLoginForm
from .models import Restaurant

def login_restaurant(request):
    if request.method == 'POST':
        form = RestaurantLoginForm(request.POST)
        if form.is_valid():
            # email = request.POST['email']
            # password = request.POST['password']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Attempting to authenticate user: {email}")

            try:
                user = authenticate(request, email=email, password=password)
                print("Email: ",email)
                print("Password: ",password)
                print(f"Authenticated user: {user}")

                if user is not None:
                    print("Authentication successful")
                    auth_login(request, user)
                    # update_last_access(user)
                    return redirect('index')
                else:
                    print("Authentication failed: Invalid credentials")
                    form.add_error(None, 'Invalid credentials')
            except Restaurant.DoesNotExist:
                print("Authentication failed: User does not exist")
                form.add_error(None, 'Invalid credentials')
    else:
        form = RestaurantLoginForm()

    return render(request, 'loginRestaurant.html', {'form': form})
