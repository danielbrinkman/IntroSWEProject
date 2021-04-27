from django.shortcuts import render, redirect
from .models import Restaurant


def home(request):
    context = {
        'restaurants': Restaurant.objects.all()
    }
    return render(request, 'restaurants/restaurant.html', context)


