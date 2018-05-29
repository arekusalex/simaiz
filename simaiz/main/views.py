from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms_sim import SimulacionForm, TerrenoForm, HumedadForm
from .multiforms import MultipleFormsView
from .models import *
from .utilidades import *


# Create your views here.

def inicio(request):
    hay_busqueda = False
    simulaciones = list()
    haySimu = Simulacion.objects.filter().exists()
    if haySimu:
        sims = Simulacion.objects.filter(compartir=True)
        nomFer = list()
        sList = list()
        for sim in sims:
            applies = Aplicacion.objects.filter(simulacion=sim)
            for ap in applies:
                nomFer.append(ap.fertilizante)
            sList.append(sim)
            sList.append(nomFer)
            simulaciones.append(sList)
            sList = []  # vaciando lista
            nomFer = []  # vaciando los nombre de los fertilizantes

    if request.method == 'POST':
        if 'f_buscar' in request.POST:
            busqueda = request.POST.get('buscar')
            search = busqueda.lower()
            simulaciones = buscar(simulaciones, search)
            if simulaciones:
                hay_busqueda = 'Resultados de la busqueda: ' + busqueda
            else:
                hay_busqueda = 'No se encontro nunguna coincidencia de: ' + busqueda
    if haySimu:
        haySimu = False
    else:
        haySimu = 'No hay ninguna simulacion que haya sido compartidas por los usuarios'
    contexto = {
        'simu': haySimu,
        'busqueda': hay_busqueda,
        'simulaciones': simulaciones,
    }
    return render(request, "main/index.html", contexto)


def ayuda(request):
    return render(request, 'ayuda.html', {})


@login_required()
def direccionar(request):
	if request.user.is_authenticated:
		return redirect('mi_espacio', username=request.user.username)
	else:
		return redirect('inicio') 

@login_required()
def mi_espacio(request, username,op='all'):
	if username == request.user.username:
		hay_busqueda=False
		if op=='all' or op=='shared' or op=='private':
			simulaciones=list()
			if op=='all':
				activo=['active','','']
				haySimu=Simulacion.objects.filter(usuario=request.user).exists()
				if haySimu:
					sims=Simulacion.objects.filter(usuario=request.user)
					nomFer=list()
					sList=list()
					for sim in sims:
						applies=Aplicacion.objects.filter(simulacion=sim)
						for ap in applies:
							nomFer.append(ap.fertilizante)
						sList.append(sim)
						sList.append(nomFer)
						simulaciones.append(sList)
						sList=[] #vaciando lista
						nomFer=[] #vaciando los nombre de los fertilizantes
				if request.method=='POST':
					if 'f_buscar' in request.POST:
						busqueda=request.POST.get('buscar')
						search=busqueda.lower()
						simulaciones=buscar(simulaciones,search)
						hay_busqueda=True
					if 'f_delete' in request.POST:
						id_sim=request.POST.get('id_sim')
						simulacion=Simulacion.objects.get(id=id_sim)
						simulacion.delete()
						return redirect('mi_espacio',username=request.user.username)

			elif op=='shared':
				activo=['','active','']
				haySimu=Simulacion.objects.filter(compartir=True,usuario=request.user).exists()
				if haySimu:
					sims=Simulacion.objects.filter(compartir=True,usuario=request.user)
					nomFer=list()
					sList=list()
					for sim in sims:
						applies=Aplicacion.objects.filter(simulacion=sim)
						for ap in applies:
							nomFer.append(ap.fertilizante)
						sList.append(sim)
						sList.append(nomFer)
						simulaciones.append(sList)
						sList=[] #vaciando lista
						nomFer=[] #vaciando los nombre de los fertilizantes
				if request.method=='POST':
					if 'f_buscar' in request.POST:
						busqueda=request.POST.get('buscar')
						search=busqueda.lower()
						simulaciones=buscar(simulaciones,search)
						hay_busqueda=True
					if 'f_delete' in request.POST:
						id_sim=request.POST.get('id_sim')
						simulacion=Simulacion.objects.get(id=id_sim)
						simulacion.delete()
						return redirect('mi_espacio_op',username=request.user.username, op='shared')
			else:
				activo=['','','active']
				haySimu=Simulacion.objects.filter(compartir=False,usuario=request.user).exists()
				if haySimu:
					sims=Simulacion.objects.filter(compartir=False,usuario=request.user)
					nomFer=list()
					sList=list()
					for sim in sims:
						applies=Aplicacion.objects.filter(simulacion=sim)
						for ap in applies:
							nomFer.append(ap.fertilizante)
						sList.append(sim)
						sList.append(nomFer)
						simulaciones.append(sList)
						sList=[] #vaciando lista
						nomFer=[] #vaciando los nombre de los fertilizantes
				if request.method=='POST':
					if 'f_buscar' in request.POST:
						busqueda=request.POST.get('buscar')
						search=busqueda.lower()
						simulaciones=buscar(simulaciones,search)
						hay_busqueda=True
					if 'f_delete' in request.POST:
						id_sim=request.POST.get('id_sim')
						simulacion=Simulacion.objects.get(id=id_sim)
						simulacion.delete()
						return redirect('mi_espacio_op',username=request.user.username, op='private')

		else:
			return redirect('mi_espacio_op', username=request.user.username, op='all')

		if hay_busqueda:
			if simulaciones:
				hay_busqueda='Resultados de la busqueda: '+busqueda
			else:
				hay_busqueda='No se encontro nunguna coincidencia de: '+busqueda
		if haySimu:
			haySimu=False
		else:
			haySimu='No se encontraron simulaciones'

		contexto = {
			'nombre': request.user.first_name+' '+request.user.last_name,
			'simu':haySimu,
			'simulaciones':simulaciones,
			'busqueda':hay_busqueda,
			'activo':activo,
		}
		return render(request, "main/mi_espacio.html", contexto)
	else:
		return redirect('mi_espacio', username=request.user.username)

def simformview(request):
    if request.method == 'POST':
        sim_form = SimulacionForm(request.POST)
        terreno_form = TerrenoForm(request.POST)
        humedad_form = HumedadForm(request.POST)
        if sim_form.is_valid() or terreno_form.is_valid() or humedad_form.is_valid():
            sim_form.save()
            terreno_form.save()
            humedad_form.save()
            return HttpResponseRedirect(redirect('sim_lista'))
        else:
            return HttpResponse('Error!')
    else:
        sim_form = SimulacionForm()
        terreno_form = TerrenoForm()
        humedad_form = HumedadForm()

    context = {
        'sim_form': sim_form,
        'terreno_form': terreno_form,
        'humedad_form': humedad_form,
    }

    return render(request, "main/SimulacionForm.html", context)
