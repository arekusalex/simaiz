from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

from main.models import Configuracion
from main.models import Fertilizante
from configuracion.forms import ConfiguracionForm
from configuracion.forms import FertilizanteForm

# Create your views here.


def configuracionSim(request):
	listaFert = list()
	hayConfi = False
	if request.method == 'POST': #ya estan cargados los formularios
		if 'btnForm1' in request.POST: #si se selecciona el boton de agregar precio
			configuracion = Configuracion.objects.filter(usuario= request.user).exists()
			if configuracion:
				hayConfi = True
				configuracion = Configuracion.objects.get(usuario= request.user)
				form1 = ConfiguracionForm(request.POST, instance = configuracion)
				form1.save()
				return redirect('configuracion')
			else:
				precio = request.POST.get('precio_maiz')
				form1 = Configuracion(usuario=request.user, precio_maiz=precio, unidadMedidaMaiz = 10)
				form1.save()
				hayConfi = True
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

		if 'inputEliminar' in request.POST:
			idEliminar = request.POST.get('inputEliminar')
			fertilizante = Fertilizante.objects.get(id =idEliminar)
			fertilizante.delete()
			return redirect('configuracion')

		if 'btnEditarFert' in request.POST:
			idEditar= request.POST.get('inputEditar')
			fertilizante = Fertilizante.objects.get(id =idEditar)
			formFertEdit = FertilizanteForm(request.POST, instance= fertilizante)
			if formFertEdit.is_valid():
				formFertEdit.save()
			return redirect('configuracion')

	else:#al cargar la pagina
		configuracion = Configuracion.objects.filter(usuario= request.user).exists()
		if configuracion:
			hayConfi = True
			configuracion = Configuracion.objects.get(usuario= request.user)
			form1 = ConfiguracionForm(instance = configuracion)
			form2 = FertilizanteForm
			
		else: #si no tiene una configuracion hecha, le carga solamente el formulario
			form1 = ConfiguracionForm
			form2 = FertilizanteForm

		#Para cargar tabla
		configuracion = Configuracion.objects.filter(usuario= request.user).exists()	
		if configuracion:
			hayConfi = True
			configuracion = Configuracion.objects.get(usuario= request.user)
			fertUsuarios = Fertilizante.objects.filter(configuracion=configuracion)
			fForm = list()
			for fer in fertUsuarios:
				fertilizantesForm = FertilizanteForm(instance= fer)
				fForm.append(fer)
				fForm.append(fertilizantesForm)
				listaFert.append(fForm)
				fForm= []
			#Para recuperar form de cada objeto
		else:
			fertUsuarios = ''
	print(hayConfi)
	contexto = {
	'configuraciones':form1,
	'fertilizantes':form2,
	'fertUsuarios':fertUsuarios,
	'listaFert': listaFert,
	'hayConfi': hayConfi,
	
	}
	return render (request, 'configuracion/configuracion.html', {'contexto':contexto})




	




