from django.urls import path
from .views import inicio, direccionar
from .views import simformview

urlpatterns = [
    path('', inicio, name="inicio"),
    path('', direccionar, name="sim_lista"),
    path('nuevo/', simformview, name="nuevo_sim"),
]