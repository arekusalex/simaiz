from django.urls import path
from .views import RegistrarUsuario
from django.contrib.auth.views import login, logout_then_login
from .views import GenerarSimulacion
urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name="registrar"),
    path('login/', login, {'template_name': 'usuarios/login.html'}, name="login"),
    path('logout/', logout_then_login, name='logout'),
    path('simulacion/', GenerarSimulacion.as_view(),name="simulacion"),
    
]
