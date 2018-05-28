from django.urls import path
from django.urls import include

#importamos la view
from .views import inicioConfig

urlpatterns = [
    path('',inicioConfig, name= "configuracion"),
]