from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    price       = models.IntegerField()
    currency    = models.CharField(max_length=32)
    picture     = models.CharField(max_length=32)