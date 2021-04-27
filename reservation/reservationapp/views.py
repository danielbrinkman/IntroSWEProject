from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def reservationView(request):
	all_reservation_items = restaurantPizzaHutItem.objects.all()
	return render(request, 'reservation.html', {'all_items':all_reservation_items})

def addReservationView(request):
	x = request.POST['peopleCount']
	y = request.POST['reservationName']
	z = request.POST['tablePref']
	requests = request.POST['comments']
	new_item = restaurantPizzaHutItem(peopleCount=x, reservationName=y, boothTable=z, comments=requests)
	new_item.save()
	return HttpResponseRedirect('/reservation/')

def deleteReservationView(request, i):
	y = restaurantPizzaHutItem.objects.get(id= i)
	y.delete()
	return HttpResponseRedirect('/reservation/')
