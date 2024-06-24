from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


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
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

import datetime
    
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                User = get_user_model()
                user = User.objects.get(username=username)
                user.last_login = datetime.datetime.now()
                user.save()
                return redirect('index')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'login.html', {'form': form})