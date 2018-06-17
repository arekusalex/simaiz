from django import forms 
from django.forms import ModelForm
from main.models import Configuracion
from main.models import Fertilizante 

unidadesDeMedida= (
			('Kg','kg'),
			('Lb','lb'),
			('qq','qq'),
			)	

class ConfiguracionForm(forms.ModelForm):
	class Meta:
		

		model = Configuracion

		fields = [
			'precio_maiz',
			'unidadMedidaMaiz',
		]

		labels = {
			'precio_maiz' : 'Precio de Venta',
			'unidadMedidaMaiz': 'Unidad de Medida',
		}
		
		widgets = {
			'precio_maiz': forms.NumberInput(attrs= {'class' : 'form-control'}),
			'unidadMedidaMaiz' : forms.Select(attrs= {'class' : 'form-control'},choices=unidadesDeMedida),
		}

class FertilizanteForm(forms.ModelForm):
	class Meta:
		model = Fertilizante
		
		fields = [
			'nombre_fertilizante',
			'porc_nitrogeno',
			'porc_fosforo',
			'porc_potasio',
			'peso',
			'unidadMedidaFert',
		]

		labels = {
			'nombre_fertilizante' : 'Fertilizante',
			'porc_nitrogeno': 'Nitrogeno (%)',
			'porc_fosforo': 'Fosforo (%)',
			'porc_potasio': 'Potacio (%)',
			'peso' : 'Peso',
			'unidadMedidaFert': 'Unidad',
		}
		
		widgets = {
			'nombre_fertilizante': forms.TextInput(attrs= {'class' : 'form-control'}),
			'porc_nitrogeno': forms.NumberInput(attrs= {'class' : 'form-control'}),
			'porc_fosforo': forms.NumberInput(attrs= {'class' : 'form-control'}),
			'porc_potasio': forms.NumberInput(attrs= {'class' : 'form-control'}),
			'peso' : forms.NumberInput(attrs= {'class' : 'form-control'}),
			'unidadMedidaFert' : forms.Select(attrs= {'class' : 'form-control'},choices=unidadesDeMedida),
		}
	
	
		