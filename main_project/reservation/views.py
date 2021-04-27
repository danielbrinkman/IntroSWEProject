from django.shortcuts import render, redirect
from .models import Reservation
from users.models import *


def home(request):
    context = {
        'reservations': Reservation.objects.all()
    }
    return render(request, 'reservation/home.html', context)

def profile(request):
    context = {
        'reservations': Reservation.objects.all()
    }
    return render(request, 'reservation/profile.html', context)


def about(request):
    return render(request, 'reservation/about.html', {'title': 'About'})


def make_reservation(request):
    return render(request, 'reservation/make_reservation.html')


def add_reservation(request):
    x = request.POST['reservationName']
    y = request.POST['peopleCount']
    z = request.POST['tablePref']
    requests = request.POST['comments']
    date = request.POST['reservationTime']
    user = request.user.username
    new_item = Reservation(reservationName=x, peopleCount=y, boothTable=z, requests=requests, date=date, user=user)
    new_item.save()
    return redirect('reservation-home')

