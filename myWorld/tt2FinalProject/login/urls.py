from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', views.custom_login_view, name='login'),

    path('regRest/', views.regRest, name='regRest'),
    ]
