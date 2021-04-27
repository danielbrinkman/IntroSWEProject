import django
from django.shortcuts import render
from django.shortcuts import render, redirect
from models import Restaurant

# Create your views here.


PizzaHut = Restaurant
setattr(PizzaHut, 'restaurantName', 'Pizza Hut')
setattr(PizzaHut, 'restaurantType', 'Pizza')
setattr(PizzaHut, 'restaurantAddress', '4589 Pizza Ave')
setattr(PizzaHut, 'restaurantPhone', 4026758903)
PizzaHut.save()

print(PizzaHut.restaurantName)