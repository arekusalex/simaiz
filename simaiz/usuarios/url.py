from django.urls import path
from .views import RegistrarUsuario
from django.contrib.auth.views import login, logout_then_login
from .views import *    
from pkg_resources import parse_version
import django
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name="registrar"),
    path('login/', login, {'template_name': 'usuarios/login.html'}, name="login"),
    path('logout/', logout_then_login, name='logout'),
    path('generar_simulacion/<id_sim>', generarSimulacion,name="simulacion"),
    url(r'^line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^line_chart/$', views.line_chart,
        name='line_chart1'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json1'),
     url(r'^line_chart/$', views.line_chart,
        name='line_chart3'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json3'),
]
