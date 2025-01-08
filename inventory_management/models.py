import datetime
from enum import Enum
from django.db import models
from django.utils.timezone import now

class Category(Enum):
    FOOD = 'food'
    KITCHEN = 'kitchen'
    CLOTHING = 'clothing'
    MOBILE = 'mobile'
    COMPUTER = 'computer'
    GENERAL = 'general'

class Movement(Enum):
    IN = 'in'
    OUT = 'out'
   
class Status(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class Supplier(models.Model):
    name=models.CharField(max_length=200,unique=True)
    email=models.CharField(max_length=200,unique=True)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=200)

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    description=models.TextField()
    category = models.CharField(max_length=20, choices=[(c.value, c.name) for c in Category])
    price=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Stock_Movement(models.Model):
    # id
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movemet_type = models.CharField(max_length=5, choices=[(c.value, c.name) for c in Movement])
    quantity=models.IntegerField(default=0)
    date=models.DateField(default=now)
    note=models.TextField()
    

class Sales(models.Model):
    # id
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=[(c.value, c.name) for c in Status])
    quantity=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
    date=models.DateField(default=now)
    