from django.contrib import admin
from .models import Driver, Customer
# Register your models here.

admin.site.register([Driver, Customer])
