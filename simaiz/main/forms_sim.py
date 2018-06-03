from django import forms
from django.forms import ModelForm
from .models import *


class SimulacionForm(ModelForm):
    class Meta:
        model = Simulacion
        fields = [
            'usuario',
            'nombre_sim',
            'fecha_siembra',
            'planta',
            'compartir',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['planta'].queryset = Planta.objects.all()

class TerrenoForm(ModelForm):
    class Meta:
        model = Terreno
        fields = [
            'area',
            'unidad',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unidad'].queryset = UnidadMedida.objects.all()

class CondicionesForm(ModelForm):
    class Meta:
        model = Condiciones
        fields = [
            'depto',
            'region',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['depto'].queryset = Departamento.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.all()


class EstSueloForm(ModelForm):
    class Meta:
        model = EstSuelo
        fields = [
            'suelo',
            'contsuelo',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['suelo'].queryset = Suelo.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contsuelo'].queryset = ContSuelo.objects.all()
