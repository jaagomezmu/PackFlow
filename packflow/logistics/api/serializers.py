from rest_framework import serializers
from logistics.models import Carrier, Customer, Package

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone_number']
        ordering = ['id'] 


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'customer', 'weight', 'dimensions', 'origin_address', 'destination_address', 'delivery_status', 'carrier']
        ordering = ['id'] 

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'vehicle_type', 'contact_number']
        ordering = ['id'] 
