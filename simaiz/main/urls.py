from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ayuda/', ayuda, name="ayuda"),
    path('crear_simulacion/', simformview, name="crear_simulacion"),
    # path('nuevo/', simformview, name="nuevo_sim"),
    path('direccionar/', direccionar, name='direccionar'),
    path('<username>/', mi_espacio, name='mi_espacio'),
    path('<username>/<op>/', mi_espacio, name='mi_espacio_op'),

]