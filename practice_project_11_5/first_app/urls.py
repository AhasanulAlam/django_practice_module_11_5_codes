
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'meals_home')
]