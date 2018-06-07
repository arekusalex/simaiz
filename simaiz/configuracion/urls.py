from django.urls import path
from django.urls import include
from django.urls import re_path

#importamos la view
from .views import configuracionSim
from .views import fertilizanteEdit
from .views import fertilizanteDelete



urlpatterns = [
    path('',configuracionSim, name= "configuracion"),
    re_path(r'^Editar/(?P<id_fertilizante>\d+)/$',fertilizanteEdit, name= "editarFertilizante"),
    re_path(r'^Eliminar/(?P<id_fertilizante>\d+)/$',fertilizanteDelete, name= "eliminarFertilizante"),
    
]