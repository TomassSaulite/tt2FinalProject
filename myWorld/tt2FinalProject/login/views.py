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
def success(request):
  template = loader.get_template('success.html')
  return HttpResponse(template.render())
