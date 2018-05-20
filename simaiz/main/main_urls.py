from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="main_inicio"),
    path('direccionar/', direccionar, name='direccionar'),
    path('<username>/', mi_espacio, name='mi_espacio'),
]
