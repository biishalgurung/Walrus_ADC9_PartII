from django.db import models

# Create your models here.

class Property(models.Model):
    property_name=models.TextField()
    price=models.IntegerField()
    property_detail=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    customer_name=models.TextField()
    customer_address=models.TextField()
    customer_phone=models.IntegerField()
    customer_details=models.TextField()
    

class Admin(models.Model):
    admin_name=models.TextField()
    admin_details=models.TextField()
    admin_phone=models.IntegerField()
    admin_address=models.TextField()

class Owner(models.Model):
    owner_name=models.TextField()
    owner_address=models.TextField()
    owner_details=models.TextField()
    owner_phone=models.IntegerField()
    uploaded_at=models.DateTimeField(auto_now_add=True)
