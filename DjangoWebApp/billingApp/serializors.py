from django.db.models import fields
from rest_framework import serializers
from billingApp.models import Bill, Bill_details, Customer, Stock,Service

class customerSerializor(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class serviceSerializor(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields="__all__"

class billSerializor(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['customer']=customerSerializor(instance.customer_id).data
        return response

class serviceDetailSerializor(serializers.ModelSerializer):
    class Meta:
        model=Bill_details
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['bill']=billSerializor(instance.bill_id).data
        response['service']=serviceSerializor(instance.service_id).data
        return response

class stockSerializor(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields="__all__"

    