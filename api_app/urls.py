from django.urls import path
from . import api_views
from . import views

# endpoints for my api
urlpatterns= [
    path('',views.index, name= 'homepage'),
    path('driver/', api_views.get_drivers, name= 'Drivers'),
    path('customer/', api_views.post_customers, name= 'Customer')
]

