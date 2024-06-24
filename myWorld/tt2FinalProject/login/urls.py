from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('get_form/', views.get_form, name='get_form'),
]
