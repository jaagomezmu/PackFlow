from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)


class Package(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='packages')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=50)
    origin_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    delivery_status = models.CharField(max_length=20)


class Carrier(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    packages = models.ManyToManyField(Package, related_name='carriers')

