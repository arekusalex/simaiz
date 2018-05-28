from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrarForm
from .forms import SimularForm
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
class RegistrarUsuario(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("main_inicio")

class GenerarSimulacion(CreateView):
	model=User
	template_name="usuarios/generar_simulacion.html"
	form_class=SimularForm
	success_url=reverse_lazy("main_inicio")

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Potasio", "Fosforo", "Magnesio"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Fertilizante1", "Fertilizante2"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                ]
class LineChartJSONView2(BaseLineChartView):
    def get_labels1(self):
        """Return 7 labels for the x-axis."""
        return ["Potasio", "Fosforo", "Magnesio"]

    def get_providers1(self):
        """Return names of datasets."""
        return ["Fertilizante1", "Fertilizante2"]

    def get_data1(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                ]
class LineChartJSONView3(BaseLineChartView):
    def get_labels3(self):
        """Return 7 labels for the x-axis."""
        return ["Potasio", "Fosforo", "Magnesio"]

    def get_providers3(self):
        """Return names of datasets."""
        return ["Fertilizante1", "Fertilizante2"]

    def get_data3(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                ]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
line_chart1 = TemplateView.as_view(template_name='line_chart.html')
line_chart_json1 = LineChartJSONView2.as_view()
line_chart3 = TemplateView.as_view(template_name='line_chart.html')
line_chart_json3 = LineChartJSONView3.as_view()