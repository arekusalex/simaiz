from django import forms 

from main.models import Configuracion
from main.models import Fertilizante 


class ConfiguracionForm(forms.ModelForm):
	class Meta:
		model = Configuracion

		fields = [
			'precio_maiz',
		]

		labels = {
			'precio_maiz' : 'Precio de Venta (qq)',
		}
		
		widgets = {
			'precio_maiz': forms.TextInput(attrs= {'class' : 'form-control'}),
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
			'nombre_fertilizante' : 'Nombre de Fertilizante',
			'porc_nitrogeno': 'Nitrogeno (%)',
			'porc_fosforo': 'Fosforo (%)',
			'porc_potasio': 'Potacio (%)',
			'peso' : 'Peso',
			'unidadMedidaFert': 'Unidades',
		}
		
		widgets = {
			'nombre_fertilizante': forms.TextInput(attrs= {'class' : 'form-control'}),
			'porc_nitrogeno': forms.TextInput(attrs= {'class' : 'form-control'}),
			'porc_fosforo': forms.TextInput(attrs= {'class' : 'form-control'}),
			'porc_potasio': forms.TextInput(attrs= {'class' : 'form-control'}),
			'peso' : forms.Select(attrs= {'class' : 'form-control'}),
			'unidadMedidaFert' : forms.Select(attrs= {'class' : 'form-control'}),
		}