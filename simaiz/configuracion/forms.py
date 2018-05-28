from django import forms 

from main.models import Configuracion


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
		