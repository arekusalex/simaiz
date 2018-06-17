from django.urls import path
from django.urls import include
from django.urls import re_path

#importamos la view
from .views import configuracionSim



urlpatterns = [
    path('',configuracionSim, name= "configuracion"),
    
    
]