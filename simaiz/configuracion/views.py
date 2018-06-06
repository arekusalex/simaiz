from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

from main.models import Configuracion
from main.models import Fertilizante
from configuracion.forms import ConfiguracionForm
from configuracion.forms import FertilizanteForm

# Create your views here.


def configuracion_precio(request):
	configuracion = Configuracion.objects.filter(usuario= request.user).exists()
	if configuracion:
		configuracion = Configuracion.objects.get(usuario= request.user)
		if request.method == 'GET':
			form = ConfiguracionForm(instance = configuracion)
		else:
			form = ConfiguracionForm(request.POST, instance = configuracion)
			form.save()
			return redirect('configuracion')
	else:
		if request.method == 'POST':
			precio = request.POST.get('precio_maiz')
			form = Configuracion(usuario=request.user, precio_maiz=precio)
			form.save()
			return redirect('configuracion')
		else:
			form= ConfiguracionForm

		form = ConfiguracionForm(request.POST)
	return render (request, 'configuracion/configuracion.html', {'form':form})

def fertilizanteCreate(request):
	if request.method == 'POST':
		#configuracion = Configuracion.objects.filter(usuario= request.user).exists()
		#if configuracion:
		configuracion = Configuracion.objects.get(usuario= request.user)
		nombreFer = request.POST.get('nombre_fertilizante')
		porcN = request.POST.get('porc_nitrogeno')
		porcK = request.POST.get('porc_potasio')
		porcP = request.POST.get('porc_fosforo')
		peso = request.POST.get('peso')
		uMed = request.POST.get('unidadMedidaFert')
		newFertilizante = Fertilizante(configuracion, nombreFer, porcN,porcK,porcP,peso,Umed)
		newFertilizante.save()
		return redirect('fertilizanteNuevo')
			#contexto = {
			#'configuracion' : Configuracion.objects.get(usuario= request.user)
			#'nombreFer' : request.POST.get('nombre_fertilizante')
			#'porcN' : request.POST.get('porc_nitrogeno')
			#'porcK'  request.POST.get('porc_potasio')
			#'porcP' : request.POST.get('porc_fosforo')
			#'peso' : request.POST.get('peso')
			#'uMed' : request.POST.get('unidadMedidaFert')
			#}
	else:
		newFertilizante = FertilizanteForm()
	return render (request, 'configuracion/configuracion.html', {'fertilizantes':newFertilizante})





