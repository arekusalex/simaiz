from django.urls import path
from django.urls import include

#importamos la view
from .views import configuracion_precio
from .views import fertilizanteCreate

urlpatterns = [
    path('',configuracion_precio, name= "configuracion"),
    path('nu/',fertilizanteCreate, name= "nuevoFertilizante"),
]