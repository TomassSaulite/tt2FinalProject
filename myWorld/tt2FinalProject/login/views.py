from django.http import HttpResponse
from django.template import loader

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())
def success(request):
  template = loader.get_template('success.html')
  return HttpResponse(template.render())

# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User created successfully')
            return redirect('success')  # Redirect to login or another page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
  
  

