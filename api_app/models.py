from django.db import models

# Create your models here.
class Driver(models.Model):
    name= models.CharField(max_length=1000000)
    age= models.CharField(max_length=1000000)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=1000000)
    age = models.CharField(max_length=1000000)
    service_choice= models.CharField(max_length=1000000)

    def __str__(self):
        return self.name
        

    