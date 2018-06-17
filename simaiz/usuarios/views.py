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

class RegistrarUsuario(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("inicio")

def generarSimulacion(request,id_sim):
    simulacion=Simulacion.objects.get(id=id_sim)
    aplicacion=Aplicacion.objects.filter(simulacion=simulacion)[0]
    area=simulacion.area
    fecha=aplicacion.fecha_app
    fertilizante=aplicacion.fertilizante
    porc_nitrogeno=aplicacion.fertilizante.porc_nitrogeno
    peso=aplicacion.fertilizante.peso
    requerimiento=Requerimiento.objects.all()[0]
    nitrogeno=requerimiento.nitrogeno
    cantidadon=cantidad_optima_nitro(nitrogeno, porc_nitrogeno,peso,area)
    context={
        'cantidad':cantidadon,
        'simulacion':simulacion,
        'fecha':fecha,
        'fertilizante':fertilizante,
        
        
    }
    return render(request,'usuarios/generar_simulacion.html',context)
    
    

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Potasio", "Fosforo", "Magnesio"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Fertilizante1", "Fertilizante2"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92],
                [41, 92, 18],
                ]
class LineChartJSONView2(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Fertika", "Surco", "Pradera"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Potasio", "Fosforo", "Magnesio"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

class LineChartJSONView3(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    def get_providers(self):
        """Return names of datasets."""
        return ["LLuvioso", "Templado", "Despejado"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35, 75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92, 41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65, 87, 21, 94, 3, 90, 13, 65,]]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
line_chart2 = TemplateView.as_view(template_name='line_chart2.html')
line_chart_json2 = LineChartJSONView2.as_view()
line_chart3 = TemplateView.as_view(template_name='line_chart3.html')
line_chart_json3 = LineChartJSONView3.as_view()

