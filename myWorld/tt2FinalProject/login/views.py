from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ClientForm, RestaurantForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientRegistrationForm, RestaurantRegistrationForm

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'client':
            form = ClientRegistrationForm(request.POST)
        else:
            form = RestaurantRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            if user_type == 'client':
                user.is_client = True
            else:
                user.is_restaurant = True
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClientRegistrationForm()  # default form

    return render(request, 'register.html', {'form': form})

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

from django.http import HttpResponse
from django.template.loader import render_to_string

def get_form(request):
    user_type = request.GET.get('user_type')
    if user_type == 'client':
        form = ClientRegistrationForm()
    else:
        form = RestaurantRegistrationForm()

    html = render_to_string('form_fields.html', {'form': form})
    return HttpResponse(html)