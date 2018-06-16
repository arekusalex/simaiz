from django import forms
from django.forms import modelformset_factory
from django.forms import ModelForm
from .models import *
from .choices import *

class SimForm(ModelForm):
    class Meta:
        model = Simulacion
        fields = [
            'usuario',
            'nombre_sim',
            'semilla',
            'fecha_siembra',
            'area',
            'unidad_long',
            'depto',
            'zona',
            'tipo_suelo',
            'nivel_p',
            'nivel_k',
            'compartir',
        ]
        widgets = {
            'unidad_long': forms.Select(attrs={'class': 'custom-select'}),
            'tipo_suelo': forms.Select(attrs={'class': 'custom-select'}),
            'nivel_p': forms.Select(attrs={'class': 'custom-select'}),
            'nivel_k': forms.Select(attrs={'class': 'custom-select'}),
            'compartir': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }

    def __init__(self, *args, **kwargs):
        super(SimForm, self).__init__(*args, **kwargs)
        self.fields['semilla'].queryset = Planta.objects.all()
        self.fields['unidad_long'].choices = UNIDAD_LONG
        self.fields['depto'].queryset = Departamento.objects.all()
        self.fields['zona'].queryset = Region.objects.all()
        self.fields['tipo_suelo'].choices = TIPO_SUELO
        self.fields['nivel_p'].choices = NIVEL
        self.fields['nivel_k'].choices = NIVEL



class AplicacionForm(ModelForm):
    class Meta:
        model = Aplicacion
        fields = [
            'simulacion',
            'planta',
            'fertilizante',
            'fecha_app',
        ]

AplicacionFormSet = modelformset_factory(Aplicacion, form=AplicacionForm, extra=1)
