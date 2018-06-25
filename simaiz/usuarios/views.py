from django.shortcuts import render_to_response
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
from datetime import datetime,timedelta,time,date
import json as simplejson
import random

class RegistrarUsuario(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("inicio")

def generarSimulacion(request,id_sim):
    simulacion=Simulacion.objects.get(id=id_sim)
    aplicacion=Aplicacion.objects.filter(simulacion=simulacion)[0]
    tipo_suelo=simulacion.tipo_suelo
    area=simulacion.area
    semilla=simulacion.semilla
    unidad_long=simulacion.unidad_long
    fecha=aplicacion.fecha_app
    nivel_k=simulacion.nivel_k
    nivel_p=simulacion.nivel_p
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
    unidadmedida=aplicacion.fertilizante.unidadMedidaFert
    if tipo_suelo == '':
        i=1
    else: 
        i=0

    (p,s,t)=obtener_requerimientos(i,semilla,nivel_k,nivel_p)
    requerimientop=Requerimiento.objects.all()[p]
    requerimientos=Requerimiento.objects.all()[s]
    requerimientot=Requerimiento.objects.all()[t]
    nitrogenop=requerimientop.nitrogeno
    fosforop=requerimientop.fosforo
    potasiop=requerimientop.potasio
    nitrogenos=requerimientos.nitrogeno
    fosforos=requerimientos.fosforo
    potasios=requerimientos.potasio
    nitrogenot=requerimientot.nitrogeno
    fosforot=requerimientot.fosforo
    potasiot=requerimientot.potasio
    areah=conversion_distancia(area,unidad_long)
    pesok=conversion_peso(peso,unidadmedida)
    porc_fosforo=aplicacion.fertilizante.porc_fosforo
    porc_potasio=aplicacion.fertilizante.porc_potasio
    cantidadofp=cantidad_optima_nutriente(fosforop,porc_fosforo,float(pesok),areah)
    cantidadonp=cantidad_optima_nutriente(nitrogenop,porc_nitrogeno,float(pesok),areah)
    cantidadopp=cantidad_optima_nutriente(potasiop,porc_potasio,float(pesok),areah)
    cantidadofs=cantidad_optima_nutriente(fosforos,porc_fosforo,float(pesok),areah)
    cantidadons=cantidad_optima_nutriente(nitrogenos,porc_nitrogeno,float(pesok),areah)
    cantidadops=cantidad_optima_nutriente(potasios,porc_potasio,float(pesok),areah)
    cantidadoft=cantidad_optima_nutriente(fosforot,porc_fosforo,float(pesok),areah)
    cantidadont=cantidad_optima_nutriente(nitrogenot,porc_nitrogeno,float(pesok),areah)
    cantidadopt=cantidad_optima_nutriente(potasiot,porc_potasio,float(pesok),areah)
    cantidadotp=suma(cantidadonp,cantidadofp,cantidadopp)
    cantidadots=suma(cantidadons,cantidadofs,cantidadops)
    cantidadott=suma(cantidadont,cantidadoft,cantidadopt)

    zona = simulacion.zona
    humedad = Humedad.objects.all()[0:12]
    regadio = list()
    regadio = []
    lluvias = list()
    lluvias = []
    i = 0
    for h in humedad:
        average = h.promedio
        lluvias.append(average)
        if average < 200:
            x = 200 - average
            regadio.append(x)
        else:
            x = 0
            regadio.append(x)
        i+=1

    datos = list()
    datos = []
    j = 0
    for j in range(len(lluvias)):
        y = [lluvias[j], regadio[j]]
        datos.append(y)

    if zona == "Valle":
        humedad = Humedad.objects.values()[0:12]
        i = 0
        for h in humedad:
            average = h.promedio
            lluvias.append(average)
            if average < 200:
                x = 200 - average
                regadio.append(x)
            else:
                x = 0
                regadio.append(x)
            i += 1
        j = 0
        for j in range(len(lluvias)):
            y = [lluvias[j], regadio[j]]
            datos.append(y)
    if zona == "Costa":
        humedad = Humedad.objects.values()[13:25]
        i = 0
        for h in humedad:
            average = h.promedio
            lluvias.append(average)
            if average < 200:
                x = 200 - average
                regadio.append(x)
            else:
                x = 0
                regadio.append(x)
            i += 1
        j = 0
        for j in range(len(lluvias)):
            y = [lluvias[j], regadio[j]]
            datos.append(y)
    if zona == "Montaña":
        humedad = Humedad.objects.values()[26:34]
        i = 0
        for h in humedad:
            average = h.promedio
            lluvias.append(average)
            if average < 200:
                x = 200 - average
                regadio.append(x)
            else:
                x = 0
                regadio.append(x)
            i += 1
        j = 0
        for j in range(len(lluvias)):
            y = [lluvias[j], regadio[j]]
            datos.append(y)

    context={
        'datos':datos,
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
        'nitrogenop':nitrogenop,
        'fosforop':fosforop,
        'potasiop':potasiop,
        'nitrogenos':nitrogenos,
        'fosforos':fosforos,
        'potasios':potasios,
        'nitrogenot':nitrogenot,
        'fosforot':fosforot,
        'potasiot':potasiot,
    }

    return render(request,'usuarios/generar_simulacion.html', context)
    
    

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Primera", "Segunda", "Tercera"]

    def get_providers(self):
        """Return names of datasets."""
        
        return ["Nitrogeno","Fosforo","Potasio"]

    def get_data(self):
        """Return 3 datasets to plot."""


        return [
                [],
                [],
                [],
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
        return ["PRECIPITACION (mm)"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [
                [5.38,4.15,16.42,57.66,203.28,329.27,239.81,296.48,354.35,211.88,48.77,11.08,0.00],
                ]

line_chart3 = TemplateView.as_view(template_name='line_chart3.html')
line_chart_json3 = LineChartJSONView3.as_view()