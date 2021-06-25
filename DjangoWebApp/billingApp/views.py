from django.http import response
from billingApp.serializors import billSerializor, customerSerializor, stockSerializor,serviceDetailSerializor,serviceSerializor
from billingApp.models import Bill, Customer, Stock,Bill_details,Service
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets
from billingApp.serializors import customerSerializor
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CutomerViewSet(viewsets.ViewSet):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def list(self,request):
        customer=Customer.objects.all()
        serializer=customerSerializor(customer,many=True,context={"request":request})
        response_dict={"error":False,"message":"All customer list data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=customerSerializor(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Customer Data saved succesfully!"}
        
        except:
            dict_response={"error":True,"message":"Error occured while saving data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Customer.objects.all()
            customer=get_object_or_404(queryset,pk=pk)
            serializer=customerSerializor(customer,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Data updated Succesfully"}
        except:
            dict_response={"error":True,"message":"Error while updating data"}
        
        return Response(dict_response)

customer_create=CutomerViewSet.as_view({"post":"create"})
customer_list=CutomerViewSet.as_view({"get":"list"})
customer_update=CutomerViewSet.as_view({"put":"update"})





class ServiceViewSet(viewsets.ViewSet):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def list(self,request):
        service=Service.objects.all()
        serializer=customerSerializor(service,many=True,context={"request":request})
        response_dict={"error":False,"message":"All service list data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=serviceSerializor(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Service Data saved succesfully!"}
        
        except:
            dict_response={"error":True,"message":"Error occured while saving data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Service.objects.all()
            service=get_object_or_404(queryset,pk=pk)
            serializer=customerSerializor(service,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Data updated Succesfully"}
        except:
            dict_response={"error":True,"message":"Error while updating data"}
        
        return Response(dict_response)

service_create=ServiceViewSet.as_view({"post":"create"})
service_list=ServiceViewSet.as_view({"get":"list"})
service_update=ServiceViewSet.as_view({"put":"update"})





class StockViewSet(viewsets.ViewSet):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def list(self,request):
        stock=Stock.objects.all()
        serializer=stockSerializor(stock,many=True,context={"request":request})
        response_dict={"error":False,"message":"All stock list data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=stockSerializor(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Stock Data saved succesfully!"}
        
        except:
            dict_response={"error":True,"message":"Error occured while saving data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Stock.objects.all()
            stock=get_object_or_404(queryset,pk=pk)
            serializer=billSerializor(stock,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Data updated Succesfully"}
        except:
            dict_response={"error":True,"message":"Error while updating data"}
        
        return Response(dict_response)

stock_create=StockViewSet.as_view({"post":"create"})
stock_list=StockViewSet.as_view({"get":"list"})
stock_update=StockViewSet.as_view({"put":"update"})