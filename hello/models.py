from django.db import models

# Create your models here.
class Product2(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    displayurl = models.CharField(max_length=1000)
    price = models.IntegerField(max_length=18)
    currency = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = '"salesforce"."product2"'