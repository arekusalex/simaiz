from django.urls import path
from .views import *
# from .views import MultipleFormsDemoView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ayuda/', ayuda, name="ayuda"),
    path('direccionar/', direccionar, name='direccionar'),
    path('<username>/', mi_espacio, name='mi_espacio'),
    path('nuevo/', MultipleFormsDemoView.as_view(), name="nuevo_sim"),
]