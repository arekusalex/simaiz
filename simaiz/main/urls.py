from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ayuda/', ayuda, name="ayuda"),
    path('direccionar/', direccionar, name='direccionar'),
    path('<username>/<op>/', mi_espacio, name='mi_espacio_op'),
    path('nuevo/', simformview, name="nuevo_sim"),
]