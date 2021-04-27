from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.home, name='reservationapp-home'),
    path('about/', views.about, name='reservationapp-about'),
    path('make_reservation/', views.make_reservation, name='make-reservationapp'),
    path('addReservationItem/', views.add_reservation),
]
