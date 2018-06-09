from django.urls import path
from django.urls import include

#importamos la view
from .views import configuracionSim


urlpatterns = [
    path('',configuracionSim, name= "configuracion"),
    
]