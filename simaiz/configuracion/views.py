from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from main.models import Configuracion
from main.models import Fertilizante
from configuracion.forms import ConfiguracionForm
from configuracion.forms import FertilizanteForm

# Create your views here.

@login_required()
def configuracionSim(request, username):
	listaFert = list()
	hayConfi = False
	precioNeg = False
	fertInval = False
	fertInvalVentana = False
	if request.method == 'POST': #ya estan cargados los formularios
		if 'btnForm1' in request.POST: #si se selecciona el boton de agregar precio
			configuracion = Configuracion.objects.filter(usuario= request.user).exists()
			if configuracion:
				hayConfi = True
				precio = float(request.POST.get('precio_maiz'))
				if precio <= 0:
					precioNeg = True
				else:
					configuracion = Configuracion.objects.get(usuario= request.user)
					form1 = ConfiguracionForm(request.POST, instance = configuracion)
					form1.save()
					return redirect('configuracion',username=request.user.username)
			else:
				precio = float(request.POST.get('precio_maiz'))
				if precio <= 0:
					precioNeg = True
				else:
					form1 = Configuracion(usuario=request.user, precio_maiz=precio, unidadMedidaMaiz = 10)
					form1.save()
					hayConfi = True
					return redirect('configuracion',username=request.user.username)
			

		if 'btnForm2' in request.POST:	
			configuracion = Configuracion.objects.get(usuario= request.user)
			nombreFer = request.POST.get('nombre_fertilizante')
			porcN = float(request.POST.get('porc_nitrogeno'))
			porcK = float(request.POST.get('porc_potasio'))
			porcP = float(request.POST.get('porc_fosforo'))
			peso = float(request.POST.get('peso'))
			uMed = request.POST.get('unidadMedidaFert')
			form2 = Fertilizante(configuracion= configuracion, nombre_fertilizante= nombreFer, porc_nitrogeno= porcN, porc_potasio= porcK,porc_fosforo= porcP,peso = peso,unidadMedidaFert=uMed)
			if (porcN < 0 or porcK <0 or porcP < 0 or peso <= 0):
				fertInval = True
			else:
				form2.save()
				return redirect('configuracion',username=request.user.username)

		if 'inputEliminar' in request.POST:
			idEliminar = request.POST.get('inputEliminar')
			fertilizante = Fertilizante.objects.get(id =idEliminar)
			fertilizante.delete()
			return redirect('configuracion',username=request.user.username)

		if 'btnEditarFert' in request.POST:
			idEditar= request.POST.get('inputEditar')

			porcN = float(request.POST.get('porc_nitrogeno'))
			porcK = float(request.POST.get('porc_potasio'))
			porcP = float(request.POST.get('porc_fosforo'))
			peso = float(request.POST.get('peso'))
			uMed = request.POST.get('unidadMedidaFert')

			if (porcN < 0 or porcK <0 or porcP < 0 or peso <= 0):
				fertInvalVentana = True
			else:
				fertilizante = Fertilizante.objects.get(id =idEditar)
				formFertEdit = FertilizanteForm(request.POST, instance= fertilizante)
				if formFertEdit.is_valid():
					formFertEdit.save()
				return redirect('configuracion',username=request.user.username)

		configuracion = Configuracion.objects.filter(usuario= request.user).exists()
		if configuracion:
			hayConfi = True
			configuracion = Configuracion.objects.get(usuario= request.user)
			form1 = ConfiguracionForm(instance = configuracion)
			form2 = FertilizanteForm
			
		else: #si no tiene una configuracion hecha, le carga solamente el formulario
			form1 = ConfiguracionForm
			form2 = FertilizanteForm

		form2 = FertilizanteForm
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
		else:
			fertUsuarios = ''

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
		
	contexto = {
	'configuraciones':form1,
	'fertilizantes':form2,
	'fertUsuarios':fertUsuarios,
	'listaFert': listaFert,
	'hayConfi': hayConfi,
	'precioNeg':precioNeg,
	'fertInval' : fertInval,
	'fertInvalVentana' : fertInvalVentana,
	}
	return render (request, 'configuracion/configuracion.html', {'contexto':contexto})




	




