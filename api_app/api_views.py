from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Driver, Customer
from .serializers import DriverSerilizer, CustomerSerilizer

# Create your views here.
@api_view(['GET'])
def get_drivers( request):
    if request.method == 'GET':
        driver= Driver.objects.all()
        driver_data= DriverSerilizer(driver, many= True)
        return Response(driver_data.data)
    else:
        return Response({"status" : "405, Permission not allowed"})

@api_view(['GET','POST'])
def post_customers( request):
    if request.method == 'GET':
        customer= Customer.objects.all()
        customer_data= CustomerSerilizer(customer, many= True)
        return Response(customer_data.data)
    elif request.method == 'POST':
        customer_data= CustomerSerilizer(data=request.data) 
        if customer_data.is_valid():
            customer_data.save()
            return Response(customer_data.data)
        return Response(customer_data.errors, status.HTTP_400_BAD_REQUEST)