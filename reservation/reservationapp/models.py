from django.db import models

# Create your models here. THESE ARE DB TABLES
class reservationItem(models.Model):
	content = models.TextField()

class restaurantPizzaHutItem(models.Model):
	peopleCount = models.TextField()
	reservationName = models.TextField()
	isReserved = True

