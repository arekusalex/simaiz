from django.urls import path
from django.urls import include

#importamos la view
from .views import configuracion_precio

urlpatterns = [
    path('',configuracion_precio, name= "configuracion"),
]