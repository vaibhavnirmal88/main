from django.db import models

class Receipts(models.Model):
    receipt_number=models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='ID' , unique=True)
    Name=models.CharField(max_length=50)
    date=models.DateField(max_length=10)
    email=models.EmailField(max_length=254)
    mobile_number=models.CharField(max_length=13)
    amount=models.CharField(max_length=5)
    years=models.CharField(max_length=9)

# Create your models here.
