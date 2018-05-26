from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView
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
	if username==request.user.username:
		contexto = {
		'nombre': request.user.first_name+' '+request.user.last_name,
		}
		return render(request, "main/mi_espacio.html", contexto)
	else:
		return redirect('mi_espacio', username=request.user.username)
	return render(request,"main/index.html",{})


class MultipleFormsDemoView(MultipleFormsView):
    template_name = "main/SimulacionForm.html"
    success_url = reverse_lazy("sim_lista")
    forms_classes = [
        SimulacionForm,
        TerrenoForm,
        HumedadForm,
    ]

    def get_forms_classes(self):
        ##forms_classes = super(MultipleFormsDemoView, self).get_forms_classes()
        return super(MultipleFormsDemoView, self).get_forms_classes()

    def form_valid(self, form):
        print("yay it's valid!")
        return super(MultipleFormsDemoView).form_valid(form)
