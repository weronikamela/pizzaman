from django.db import models

# Create your models here.
class Product2(models.Model):
    id           = models.IntegerField(unique=True)
    name         = models.CharField(max_length=255, db_column='name')
    url          = models.CharField(max_length=1000, db_column='displayurl')
    price        = models.DecimalField(max_digits=18, decimal_places=2, db_column='price__c')
    currency     = models.CharField(max_length=5, db_column='currency__c')
    description  = models.CharField(max_length=255, db_column='description__c')
    sfid         = models.CharField(primary_key=True, max_length=18, db_column='sfid')
    class Meta:
        managed = False
        db_table = '"salesforce"."product2"'

class Order(models.Model):
    # id          = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=255, db_column='cst_name__c')
    surname     = models.CharField(max_length=255, db_column='cst_surname__c')
    street      = models.CharField(max_length=255, db_column='cst_street__c')
    postalcode  = models.CharField(max_length=32, db_column='cst_postal_code__c')
    city        = models.CharField(max_length=80, db_column='cst_city__c')
    email       = models.EmailField(max_length=80, db_column='cst_email__c')
    phone       = models.CharField(max_length=40, db_column='cst_phone__c')
    product     = models.OneToOneField(Product2, db_column='productid__c')
    class Meta:
        managed = False
        db_table = '"salesforce"."order__c"'
