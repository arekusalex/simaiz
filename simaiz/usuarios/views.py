from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrarForm
from .forms import SimularForm
from random import randint
from main.models import *
from main.views import *
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from datetime import datetime,timedelta

class RegistrarUsuario(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("inicio")

def generarSimulacion(request,id_sim):
    simulacion=Simulacion.objects.get(id=id_sim)
    aplicacion=Aplicacion.objects.filter(simulacion=simulacion)[0]
    area=simulacion.area
    unidad_long=simulacion.unidad_long
    fecha=aplicacion.fecha_app
    dia1=timedelta(days=10)
    dia2=timedelta(days=25)
    dia3=timedelta(days=40)
    fecha1=fecha+dia1
    fecha2=fecha+dia2
    fecha3=fecha+dia3
    fertilizante=aplicacion.fertilizante
    conf=Configuracion.objects.all()[0]
    precio=aplicacion.fertilizante.configuracion.precio_maiz
    porc_nitrogeno=aplicacion.fertilizante.porc_nitrogeno
    peso=aplicacion.fertilizante.peso
    unidadmedida=aplicacion.fertilizante.peso
    requerimiento=Requerimiento.objects.all()[0]
    nitrogeno=requerimiento.nitrogeno
    fosforo=requerimiento.fosforo
    potasio=requerimiento.potasio
    areah=conversion_distancia(area,unidad_long)
    pesok=conversion_peso(peso,unidadmedida)
    porc_fosforo=aplicacion.fertilizante.porc_fosforo
    porc_potasio=aplicacion.fertilizante.porc_potasio
    cantidadofp=cantidad_optima_nutriente(fosforo,porc_fosforo,float(pesok),areah)
    cantidadonp=cantidad_optima_nutriente(nitrogeno,porc_nitrogeno,float(pesok),areah)
    cantidadopp=cantidad_optima_nutriente(potasio,porc_potasio,float(pesok),areah)
    cantidadotp=suma(cantidadonp,cantidadofp,cantidadopp)
    cantidadots=suma2(cantidad_optima_nutriente(nitrogeno,porc_fosforo,float(pesok),areah),cantidad_optima_nutriente(fosforo,porc_fosforo,float(pesok),areah))
    cantidadott=cantidad_optima_nutriente(nitrogeno,porc_nitrogeno,float(pesok),areah)
    context={
        'cantidad':cantidadotp,
        'simulacion':simulacion,
        'fecha':fecha,
        'fertilizante':fertilizante,
        'fecha1':fecha1,
        'fecha2':fecha2,
        'fecha3':fecha3,
        'cantidad2':cantidadots,
        'cantidad3':cantidadott,
        'precio':precio,
        'peso':peso,
    }
    return render(request,'usuarios/generar_simulacion.html',context)
    
    

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Primera", "Segunda", "Tercera"]

    def get_providers(self):
        """Return names of datasets."""
        
        return ["Nitrogeno","Fosforo","Potasio"]

    def get_data(self):
        """Return 3 datasets to plot."""
        requerimiento=Requerimiento.objects.all()[0]
        nitrogeno=requerimiento.nitrogeno
        fosforo=requerimiento.fosforo
        potasio=requerimiento.potasio

        return [
                [nitrogeno,fosforo,potasio],
                [nitrogeno,fosforo],
                [nitrogeno]
                ]
class LineChartJSONView2(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""

        return ["Primera", "Segunda", "Tercera"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Totales de nutrientes"]

    def get_data(self):
        """Return 3 datasets to plot."""
        requerimiento=Requerimiento.objects.all()[0]
        nitrogeno=requerimiento.nitrogeno
        fosforo=requerimiento.fosforo
        potasio=requerimiento.potasio
        total1=nitrogeno+fosforo+potasio
        total2=nitrogeno+fosforo
        total3=nitrogeno
        return [[total1,total2,total3,0.0],
                ]

class LineChartJSONView3(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    def get_providers(self):
        """Return names of datasets."""
        return ["PRECIPITACION MEDIA ANUAL EN EL SALVADOR (mm)"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [
                [5.38,4.15,16.42,57.66,203.28,329.27,239.81,296.48,354.35,211.88,48.77,11.08,0.00],
                ]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
line_chart2 = TemplateView.as_view(template_name='line_chart2.html')
line_chart_json2 = LineChartJSONView2.as_view()
line_chart3 = TemplateView.as_view(template_name='line_chart3.html')
line_chart_json3 = LineChartJSONView3.as_view()

