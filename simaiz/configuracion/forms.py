from django import forms 
from main.models import Configuracion


class ConfiguracionForm(form.ModelForm):
	class Meta:
		model = Configuracion

		fields = [
			'precio_maiz',
		]

		labels = [
			'precio_maiz' : 'Precio de Venta',
		]
		widgets = [
			'precio_maiz': forms.TextInput(attrs= {'class' : 'form-control'}),
		]