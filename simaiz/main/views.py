from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.views.generic import FormView
from django.urls import reverse_lazy
#from .forms_sim import SimulacionForm, TerrenoForm, HumedadForm
#from .multiforms import MultipleFormsView
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .forms_sim import *
from .models import *
from .utilidades import *
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User



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
		return redirect('mi_espacio_op', username=request.user.username)


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='generar_simulacion.html')
line_chart_json = LineChartJSONView.as_view()


class SimFormView(CreateView):
    model = Simulacion
    template_name = "main/simform.html"
    form_class = SimForm
    success_url = reverse_lazy("crear_app")

    def get_context_data(self, **kwargs):
        context = super(SimFormView, self).get_context_data(**kwargs)
        context['plantas'] = Planta.objects.all()
        context['deptos'] = Departamento.objects.all()
        context['regions'] = Region.objects.all()

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse('Error!')

def load_regions(request):
    region_id = request.GET.get('zona')
    regions = Region.objects.filter(region_id=region_id).order_by('zona')
    return render(request, 'main/regions_options.html', {'regions': regions})


class AplicacionView(CreateView):
    model = Aplicacion
    template_name = "main/simform3.html"
    form_class = AplicacionForm
    success_url = reverse_lazy("direccionar")



