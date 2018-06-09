from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

from main.models import Configuracion
from main.models import Fertilizante
from configuracion.forms import ConfiguracionForm
from configuracion.forms import FertilizanteForm

# Create your views here.


def configuracionSim(request):
	if request.method == 'POST': #ya estan cargados los formularios
		if 'btnForm1' in request.POST: #si se selecciona el boton de agregar precio
			configuracion = Configuracion.objects.filter(usuario= request.user).exists()
			if configuracion:
				configuracion = Configuracion.objects.get(usuario= request.user)
				form1 = ConfiguracionForm(request.POST, instance = configuracion)
				form1.save()
				return redirect('configuracion')
			else:
				precio = request.POST.get('precio_maiz')
				form1 = Configuracion(usuario=request.user, precio_maiz=precio, unidadMedidaMaiz = 10)
				form1.save()
				return redirect('configuracion')
			

		if 'btnForm2' in request.POST:	
			configuracion = Configuracion.objects.get(usuario= request.user)
			nombreFer = request.POST.get('nombre_fertilizante')
			porcN = request.POST.get('porc_nitrogeno')
			porcK = request.POST.get('porc_potasio')
			porcP = request.POST.get('porc_fosforo')
			peso = request.POST.get('peso')
			uMed = request.POST.get('unidadMedidaFert')
			form2 = Fertilizante(configuracion= configuracion, nombre_fertilizante= nombreFer, porc_nitrogeno= porcN, porc_potasio= porcK,porc_fosforo= porcP,peso = 20,unidadMedidaFert="Kg")
			form2.save()
			return redirect('configuracion')

	else:#al cargar la pagina

		configuracion = Configuracion.objects.filter(usuario= request.user).exists()
		if configuracion:
			configuracion = Configuracion.objects.get(usuario= request.user)
			form1 = ConfiguracionForm(instance = configuracion)
			form2 = FertilizanteForm
			
		else: #si no tiene una configuracion hecha, le carga solamente el formulario
			form1 = ConfiguracionForm
			form2 = FertilizanteForm


	configuracion = Configuracion.objects.filter(usuario= request.user).exists()	
	if configuracion:
		configuracion = Configuracion.objects.get(usuario= request.user)
		fertUsuarios = Fertilizante.objects.filter(configuracion=configuracion)
	else:
		fertUsuarios = ''
	contexto = {
	'configuraciones':form1,
	'fertilizantes':form2,
	'fertUsuarios':fertUsuarios,
	
	
	}
	return render (request, 'configuracion/configuracion.html', {'contexto':contexto})

def fertilizanteEdit(request, id_fertilizante):
	fertilizante = Fertilizante.objects.get(id =id_fertilizante)
	if request.method == 'GET':
		formFertEdit =FertilizanteForm(instance=fertilizante)
	else:
		formFertEdit = FertilizanteForm(request.POST, instance= fertilizante)
		if formFertEdit.is_valid():
			formFertEdit.save()
		return redirect('configuracion')
	return render(request,'configuracion/EditFertilizante.html', {'contexto': formFertEdit})

def  fertilizanteDelete(request, id_fertilizante):
	fertilizante = Fertilizante.objects.get(id =id_fertilizante)
	if request.method == 'POST':
		fertilizante.delete()
		return redirect('configuracion')
	return render(request,'configuracion/deleteFertilizante.html',{'fertilizante':fertilizante})


	




