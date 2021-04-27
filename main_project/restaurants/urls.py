from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('add-restaurant/', views.addRestaurant, name = "add-stud"),
]
