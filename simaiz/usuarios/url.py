from django.urls import path
from .views import RegistrarUsuario
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name="registrar"),
    path('login/', login, {'template_name': 'usuarios/login.html'}, name="login"),
    path('logout/', logout_then_login, name='logout'),
]
