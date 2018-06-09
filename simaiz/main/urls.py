from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ayuda/', ayuda, name="ayuda"),
    path('crear_simulacion/', SimFormView.as_view(), name="crear_simulacion"),
    path('ajax/load-regions/', load_regions, name='ajax_load_regions'),
    path('crear_app/', AplicacionView.as_view(), name="crear_app"),
    path('direccionar/', direccionar, name='direccionar'),
    path('<username>/', mi_espacio, name='mi_espacio'),
    path('<username>/<op>/', mi_espacio, name='mi_espacio_op'),

]