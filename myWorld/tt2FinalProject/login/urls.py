from django.urls import path
from . import views
from .views import SignUpView
from .views import register_restaurant, login_restaurant


urlpatterns = [
    path('', views.index, name='index'),
    path('register/user/', SignUpView.as_view(), name='register'),
    path('login/user', views.custom_login_view, name='login'),
    path('register/restaurant/', register_restaurant, name='registerRestaurant'),
    path('login/restaurant', login_restaurant, name='loginRestaurant'),
    ]
