from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms_sim import SimulacionForm, TerrenoForm, HumedadForm
from .multiforms import MultipleFormsView


# Create your views here.

def inicio(request):
    return render(request, "main/index.html", {})


def direccionar(request):
    if request.user:
        return redirect('mi_espacio', username=request.user.username)
    else:
        return redirect('login')


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