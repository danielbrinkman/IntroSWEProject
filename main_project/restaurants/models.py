from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurantName = models.TextField()
    restaurantType = models.TextField()
    restaurantAddress = models.TextField()
    restaurantPhone = models.IntegerField()
