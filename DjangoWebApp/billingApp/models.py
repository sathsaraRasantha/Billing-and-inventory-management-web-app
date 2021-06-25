from django.db import models

# Create your models here.

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    added_on=models.DateField(auto_now_add=True)
    objects=models.Manager()

class Service(models.Model):
    id=models.AutoField(primary_key=True)
    laptop_name=models.CharField(max_length=255)
    serial_number=models.CharField(max_length=255)
    service_type=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    amount=models.IntegerField()
    objects=models.Manager()

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on=models.DateField(auto_now_add=True)
    objects=models.Manager()

class Bill_details(models.Model):
    id=models.AutoField(primary_key=True)
    service_id=models.ForeignKey(Service, on_delete=models.CASCADE)
    bill_id=models.ForeignKey(Bill, on_delete=models.CASCADE)
    description=models.CharField(max_length=255) 
    amount=models.IntegerField()
    added_on=models.DateField(auto_now_add=True)
    objects=models.Manager()

class Stock(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    buy_price=models.IntegerField()
    sell_price=models.IntegerField()
    serial_number=models.CharField(max_length=255)
    description=models.CharField(max_length=255) 
    objects=models.Manager()    
