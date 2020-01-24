from django.db import models

# Create your models here.

class Property(models.Model):
    property_name=models.TextField()
    price=models.IntegerField()
    property_detail=models.TextField()
    uploaded_at=models.DateTimeField(auto_now_add=True)