from django.db import models


class Restaurant(models.Model):
    name = models.TextField()
    type = models.TextField()
    address = models.TextField()
    phone = models.TextField()
