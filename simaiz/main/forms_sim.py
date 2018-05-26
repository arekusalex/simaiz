from django import forms
from django.forms import ModelForm
from .models import Simulacion, Planta, Suelo, UnidadMedida, Aplicacion, \
    Terreno, Departamento, Region, Humedad, Fertilizante


class SimulacionForm(forms.Form):
    class Meta:
        model = Simulacion
        fields = [
            'nombre_sim',
            'fecha_siembra',
            'planta',
        ]

class TerrenoForm(forms.Form):
    class Meta:
        model = Terreno
        fields = [
            'area',
            'unidad',
            'suelo',
            'depto',
        ]

class HumedadForm(forms.Form):
    class Meta:
        model = Humedad
        fields = [
            'region',
        ]
        widgets = {
            'region': forms.Select(attrs={'class':'form_control'}),
        }


class AplicacionForm(forms.Form):
    class Meta:
        model = Aplicacion
        fields = [
            'terreno',
            'planta',
            'fertilizante',
        ]
