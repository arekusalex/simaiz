from django import forms
from django.forms import ModelForm
from .models import Simulacion, Planta, Suelo, UnidadMedida, Aplicacion, \
    Terreno, Departamento, Region, Humedad, Fertilizante


class SimulacionForm(ModelForm):
    class Meta:
        model = Simulacion
        fields = [
            'nombre_sim',
            'fecha_siembra',
            'planta',
        ]

class TerrenoForm(ModelForm):
    class Meta:
        model = Terreno
        fields = [
            'area',
            'unidad',
            'suelo',
            'depto',
        ]

class HumedadForm(ModelForm):
    class Meta:
        model = Humedad
        fields = [
            'region',
        ]
        widgets = {
            'region': forms.Select(attrs={'class':'form_control'}),
        }


class AplicacionForm(ModelForm):
    class Meta:
        model = Aplicacion
        fields = [
            'fertilizante',
        ]
