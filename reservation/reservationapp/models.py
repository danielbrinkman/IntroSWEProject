from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reservation(models.Model):
    reservationName = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    peopleCount = models.IntegerField()
    boothTable = models.TextField()
    requests = models.TextField()
    user = models.TextField()


