from collections import namedtuple
from rest_framework import serializers
from .models import Driver, Customer

#serializing my databases to render in my prefered format(JSON, precisely)
class DriverSerilizer(serializers.ModelSerializer):
    class Meta:
        model= Driver
        fields= ('id','name', 'age')



class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= ('id','name', 'age', 'service_choice')

        