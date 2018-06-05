from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

from main.models import Configuracion
from configuracion.forms import ConfiguracionForm

# Create your views here.


def configuracion_precio(request):
	configuracion = Configuracion.objects.filter(usuario= request.user).exists()
	if configuracion:
		configuracion = Configuracion.objects.get(usuario= request.user)
		if request.method == 'GET':
			form = ConfiguracionForm(instance = configuracion)
		else:
			form = ConfiguracionForm(request.POST, instance = configuracion)
			if form.is_valid():
				form.save()
			return redirect('configuracion')
	else:
		if request.method == 'POST':
			precio = request.POST.get('precio_maiz')
			form = Configuracion(usuario=request.user, precio_maiz=precio)
			if form.is_valid:
				form.save()
			return redirect('configuracion')
		else:
			form= ConfiguracionForm

		form = ConfiguracionForm(request.POST)
	return render (request, 'configuracion/configuracion.html', {'form':form})





