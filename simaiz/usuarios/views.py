from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrarForm
from .forms import SimularForm
class RegistrarUsuario(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy("main_inicio")

class GenerarSimulacion(CreateView):
	model=User
	template_name="usuarios/generar_simulacion.html"
	form_class=SimularForm
	success_url=reverse_lazy("main_inicio")