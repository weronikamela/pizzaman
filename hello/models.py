from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    price       = models.IntegerField()
    currency    = models.CharField(max_length=32)
    picture     = models.CharField(max_length=255)

class Order(models.Model):
    cst_name        = models.CharField(max_length=32)
    cst_surname     = models.CharField(max_length=32)
    cst_phone       = models.CharField(max_length=32)
    cst_email       = models.CharField(max_length=32)
    cst_city        = models.CharField(max_length=32)
    cst_street      = models.CharField(max_length=32)
    cst_postal_code = models.CharField(max_length=32)
    productID       = models.CharField(max_length=32)