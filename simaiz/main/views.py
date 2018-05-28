from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms_sim import SimulacionForm, TerrenoForm, HumedadForm
from .multiforms import MultipleFormsView
from .models import *


# Create your views here.

def inicio(request):
	return render(request, "main/index.html", {})
def ayuda(request):
	return render(request,'ayuda.html',{})

@login_required()
def direccionar(request):
	if request.user.is_authenticated:
		return redirect('mi_espacio', username=request.user.username)
	else:
		return redirect('inicio') 

@login_required()
def mi_espacio(request, username):
    if username == request.user.username:
        contexto = {
            'nombre': request.user.first_name + ' ' + request.user.last_name,
        }
        return render(request, "main/mi_espacio.html", contexto)
    else:
        return redirect('mi_espacio', username=request.user.username)
    return render(request, "main/index.html", {})

    if username == request.user.username:
        simulaciones = list()
        if request.method == 'POST':
            pass
        haySimu = Simulacion.objects.filter(usuario=request.user).exists()
        if haySimu:
            sims = Simulacion.objects.filter(usuario=request.user)
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

        contexto = {
            'nombre': request.user.first_name + ' ' + request.user.last_name,
            'simu': haySimu,
            'simulaciones': simulaciones,
        }
        return render(request, "main/mi_espacio.html", contexto)
    else:
        return redirect('mi_espacio', username=request.user.username)

# def config(request):

# 	if request.method='POST': #solo se metera cuando envien un formulario
# 		precio=request.POST.get('input_precio_maiz') #obtener el valor que ingreso el user en el form
# 		config=Configuracion.objects.filter(usuario=request.user) #extraer solo la config del user
# 		config.precio_maiz=precio #setiar el valor que metio el user
# 		config.save()  #guardar todo los cambios

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

