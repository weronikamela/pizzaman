from django.db import models

# Create your models here.
class Product2(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=1000, db_column='displayurl')
    price = models.IntegerField(max_length=18, db_column='price__c')
    currency = models.CharField(max_length=5, db_column='currency__c')
    description = models.CharField(max_length=255, db_column='description__c')
    class Meta:
        managed = False
        db_table = '"salesforce"."product2"'