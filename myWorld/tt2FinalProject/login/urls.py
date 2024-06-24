from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    ]
