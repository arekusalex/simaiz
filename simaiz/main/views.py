from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.views.generic import FormView
from django.urls import reverse_lazy
from random import randint
from django.views.generic import TemplateView
from simaiz.chartjs.views.lines import BaseLineChartView
from .forms_sim import *
from .models import *
from .utilidades import *
from .choices import *
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
import datetime



# Create your views here.

def inicio(request):
    global bloqueo
    bloqueo=False #variable que domina el bloqueo del tiempo
    tiempo_pagina(0)
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
        'tiempo':tiempo_pagina(1),
    }
    return render(request, "main/index.html", contexto)

def ayuda(request):
    tiempo_pagina(0)
    contexto = {
        'tiempo':tiempo_pagina(1),
    }
    return render(request, 'index.html', contexto)


@login_required()
def direccionar(request):
    if request.user.is_authenticated:
        return redirect('mi_espacio', username=request.user.username)
    else:
        return redirect('inicio')

@login_required()
def mi_espacio(request, username,op='all'):
    agregarDeptosDB() ## metodo para agregar los 14 departamentos
    if username == request.user.username:
        tiempo_pagina(0)
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

            elif op == 'shared':
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
            'tiempo':tiempo_pagina(1),
        }
        return render(request, "main/mi_espacio.html", contexto)
    else:
        return redirect('mi_espacio', username=request.user.username)

@login_required()
def crear_simulacion(request, username):
    if username == request.user.username:
        tiempo_pagina(0)
        mod=False
        semi=list()
        semillas=list()
        semis=Planta.objects.all()
        for sem in semis:
            semi.append(sem)
            semi.append(sem.dias_ciclo)
            semillas.append(semi)
            semi=[]

        unidades=UNIDAD_LONG
        departamentos=Departamento.objects.all()
        zonas=ZONA
        suelos=TIPO_SUELO
        nutrientes=NIVEL

        try:
            ferPublicos=User.objects.get(id=2)
            configPub=Configuracion.objects.get(usuario=ferPublicos)
        except:
            redirect('mi_espacio',username=request.user.username)
        try:
            configUser=Configuracion.objects.get(usuario=request.user)
        except:
            redirect('configuracion', username=request.user.username)

        ferPub=Fertilizante.objects.filter(configuracion=configPub)
        ferUser=Fertilizante.objects.filter(configuracion=configUser)

        fertilizantes=list()
        for f in ferPub:
            fertilizantes.append(f)
        for f in ferUser:
            fertilizantes.append(f)

        if request.method=='POST': #guardar y direccionar
            if 'f_crear_simu' in request.POST:
                name=request.POST.get('name_simu')
                planta=Planta.objects.get(id=request.POST.get('semilla'))
                fecha_siembra=request.POST.get('fecha_siembra')
                area=request.POST.get('area')
                unidad=request.POST.get('unidad_long')
                depto=request.POST.get('depto')
                zona=request.POST.get('zona')
                analisis=request.POST.get('analisis')
                if analisis=='si_analisis':
                    nivel_p=request.POST.get('fosforo')
                    nivel_k=request.POST.get('potasio')
                    tipo_suelo=''
                else:
                    tipo_suelo=request.POST.get('tipo_suelo')
                    nivel_p=''
                    nivel_k=''
                compartir=True if request.POST.get('compartir') else False
                simulacion=Simulacion(usuario=request.user,nombre_sim=name, semilla=planta.nombre_planta,fecha_siembra=fecha_siembra,
                    area=area,unidad_long=unidad,depto=depto, zona=zona,tipo_suelo=tipo_suelo,nivel_p=nivel_p,nivel_k=nivel_k,
                    compartir=compartir)
                simulacion.save()

                fer1=Fertilizante.objects.get(id=request.POST.get('apply_1'))
                fer2=Fertilizante.objects.get(id=request.POST.get('apply_2'))
                fer3=Fertilizante.objects.get(id=request.POST.get('apply_3'))
                print(fecha_siembra)
                apply1=Aplicacion(simulacion=simulacion,planta=planta, fertilizante=fer1,
                    fecha_app=datetime.datetime.strptime(fecha_siembra,'%Y-%m-%d')+datetime.timedelta(days=planta.dias_ciclo*1))
                apply1.save()
                apply2=Aplicacion(simulacion=simulacion,planta=planta, fertilizante=fer2,
                    fecha_app=datetime.datetime.strptime(fecha_siembra,'%Y-%m-%d')+datetime.timedelta(days=planta.dias_ciclo*2))
                apply2.save()
                apply3=Aplicacion(simulacion=simulacion,planta=planta, fertilizante=fer3,
                    fecha_app=datetime.datetime.strptime(fecha_siembra,'%Y-%m-%d')+datetime.timedelta(days=planta.dias_ciclo*3))
                apply3.save()
                return redirect('mi_espacio', username=request.user.username)
        contexto={
            'mod':mod,
            'semillas':semillas,
            'unidades':unidades,
            'deptos':departamentos,
            'zonas':zonas,
            'suelos':suelos,
            'nutrientes':nutrientes,
            'fertilizantes':fertilizantes,
            'tiempo':tiempo_pagina(1),
        }
        return render(request, 'main/crear_simu.html', contexto)
    else:
        return redirect('crear_simu', username=request.user.username)


@login_required()
def mod_simulacion(request, username,id):
    if username == request.user.username:
        tiempo_pagina(0)
        mod=True
        semi=list()
        semillas=list()
        semis=Planta.objects.all()
        for sem in semis:
            semi.append(sem)
            semi.append(sem.dias_ciclo)
            semillas.append(semi)
            semi=[]
        unidades=UNIDAD_LONG
        departamentos=Departamento.objects.all()
        zonas=ZONA
        suelos=TIPO_SUELO
        nutrientes=NIVEL

        try:
            ferPublicos=User.objects.get(id=2)
            configPub=Configuracion.objects.get(usuario=ferPublicos)
        except:
            redirect('mi_espacio',username=request.user.username)
        try:
            configUser=Configuracion.objects.get(usuario=request.user)
        except:
            redirect('configuracion', username=request.user.username)

        ferPub=Fertilizante.objects.filter(configuracion=configPub)
        ferUser=Fertilizante.objects.filter(configuracion=configUser)

        fertilizantes=list()
        for f in ferPub:
            fertilizantes.append(f)
        for f in ferUser:
            fertilizantes.append(f)

        #fertilizantes=Fertilizante.objects.all()
        analisis=False
        fertis=list()
        fecha=''
        alerta=''
        existeSim=Simulacion.objects.filter(id=id).exists()
        if existeSim:
            if request.method == 'POST':
                sim=Simulacion.objects.get(id=id)
                sim.nombre_sim=request.POST.get('name_simu')
                sim.semilla=Planta.objects.get(id=request.POST.get('semilla')).nombre_planta
                planta=Planta.objects.get(id=request.POST.get('semilla'))
                sim.fecha_siembra=request.POST.get('fecha_siembra')
                sim.area=request.POST.get('area')
                sim.unidad_long=request.POST.get('unidad_long')
                sim.depto=request.POST.get('depto')
                sim.zona=request.POST.get('zona')
                analisis=request.POST.get('analisis')
                if analisis=='si_analisis':
                    sim.nivel_p=request.POST.get('fosforo')
                    sim.nivel_k=request.POST.get('potasio')
                    sim.tipo_suelo=''
                else:
                    sim.tipo_suelo=request.POST.get('tipo_suelo')
                    sim.nivel_p=''
                    sim.nivel_k=''
                sim.compartir=True if request.POST.get('compartir') else False
                sim.save()


                fer1=Fertilizante.objects.get(id=request.POST.get('apply_1'))
                fer2=Fertilizante.objects.get(id=request.POST.get('apply_2'))
                fer3=Fertilizante.objects.get(id=request.POST.get('apply_3'))

                fers=list()
                fers.append(fer1)
                fers.append(fer2)
                fers.append(fer3)

                applies=Aplicacion.objects.filter(simulacion=sim).order_by('fecha_app')

                for num,ap in enumerate(applies):
                    ap.fertilizante=fers[num]
                    ap.fecha_app=datetime.datetime.strptime(sim.fecha_siembra,'%Y-%m-%d')+datetime.timedelta(days=planta.dias_ciclo*num)
                    ap.save()

                alerta='La Simulacion se modifico con exito'
            #else: 
            sim=Simulacion.objects.get(id=id)
            if sim.tipo_suelo =='':
                analisis=True
            applies=Aplicacion.objects.filter(simulacion=sim)
            for ap in applies:
                fertis.append(ap.fertilizante)
            contexto={
                'mod':mod,
                'semillas':semillas,
                'unidades':unidades,
                'deptos':departamentos,
                'zonas':zonas,
                'suelos':suelos,
                'nutrientes':nutrientes,
                'fertilizantes':fertilizantes,
                'analisis':analisis,
                'sim':sim,
                'fertis':fertis,
                'fecha_siembra':str(sim.fecha_siembra),
                'alerta':alerta,
                'tiempo':tiempo_pagina(1),
            }
            return render(request, 'main/crear_simu.html', contexto)
        else:
            return HttpResponse('La simulacion a modificar no existe')
    else:
        return redirect('mod_simu', username=request.user.username, id=id)


class SimFormView(CreateView):
    model = Simulacion
    template_name = "main/simform.html"
    form_class = SimForm
    success_url = reverse_lazy('crear_app')

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
    form_class = AplicacionForm()
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("direccionar")

    def get_context_data(self, **kwargs):
        context = super(AplicacionView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        aplicacion_form_set = AplicacionFormSet()
        return self.render_to_response(self.get_context_data(aplicacion_form_set=aplicacion_form_set))

    def post(self, request, *args, **kwargs):
        aplicacion_form_set = AplicacionFormSet(request.POST)
        if aplicacion_form_set.is_valid():
            return self.form_valid(aplicacion_form_set)
        else:
            return self.form_invalid(aplicacion_form_set)

    def form_valid(self, aplicacion_form_set):
        aplicacion_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, aplicacion_form_set):
        return self.render_to_response(self.get_context_data(aplicacion_form_set=aplicacion_form_set))


def conversion_distancia(area,unidad_long):
    if unidad_long == "m²":
        conversion =  10000/area
    if unidad_long == "mz":
        conversion = area * 0.7050
    if unidad_long == "ha":
        conversion = area
    return conversion

def conversion_peso(peso,unidad):
    if unidad == "Lb" or unidad == "lb":
        conversionpeso = peso / 2.20
    if unidad == "qq" or unidad == "qq":
        conversionpeso = peso / 35.274
    if unidad == "Kg" or unidad == "kg":
        conversionpeso = peso
    return conversionpeso

def cantidad_optima_nutriente(nutriente,porc_nutriente,peso,area):
    try:
        bolsa=nutriente/(0.5*porc_nutriente)
        cantidadoptiman=(bolsa*peso)/area
        return ' %.2f' %cantidadoptiman
    except:
        return 0

def suma(valor1,valor2,valor3):
    total=float(valor1)+float(valor2)+float(valor3)
    return '%.2f' %total
def suma2(valor1,valor2):
    total=float(valor1)+float(valor2)
    return '%.2f' %total


def sin_analisis_suelo(planta):
    semilla = planta


def analisis_de_suelo(nivel_k,nivel_p):
    if nivel_k == 'Alto' & nivel_p == 'Alto':
        nitrogeno=40.53
        fosforo=0.0
        potasio=0.0
        porc_nitrogeno=21
        porc_potasio=0.0
        porc_fosforo=0.0
    if nivel_p == 'Deficiente' & nivel_k=='Deficiente':
        nitrogeno=38.60
        fosforo=38.60
        potasio=38.60
        porc_nitrogeno=15
        porc_potasio=15
        porc_fosforo=15
    return (nitrogeno,fosforo,potasio,porc_nitrogeno,porc_potasio,porc_fosforo)


def obtener_requerimientos(analisis,semilla,nivel_k,nivel_p):
    if analisis == 0: 
        if semilla == 'Oro Blanco':
            fer1=0
            fer2=1
            fer3=2
        if semilla == 'Platino':
            fer1=3
            fer2=4
            fer3=5
        if semilla == 'ASG':
            fer1=6
            fer2=7
            fer3=8
        if semilla == 'Centa':
            fer1=9
            fer2=10
            fer3=11
    else:
        if nivel_p == 'Alto' and nivel_k == 'Alto':
            if semilla == 'Oro Blanco': 
                fer1=0
                fer2=10
                fer3=2
            if semilla == 'Platino':
                fer1=3
                fer2=10
                fer3=5
            if semilla == 'ASG':
                fer1=6
                fer2=10
                fer3=8
            if semilla == 'Centa':
                fer1=9
                fer2=10
                fer3=11
        else:
            if nivel_p == 'Medio' and nivel_k == 'Alto':
                if semilla == 'Oro Blanco': 
                    fer1=6
                    fer2=10
                    fer3=2
                if semilla == 'Platino':
                    fer1=6
                    fer2=10
                    fer3=5
                if semilla == 'ASG':
                    fer1=6
                    fer2=10
                    fer3=8
                if semilla == 'Centa':
                    fer1=6
                    fer2=10
                    fer3=11
            else:
                if nivel_p == 'Deficiente' and nivel_k == 'Deficiente':
                    if semilla == 'Oro Blanco': 
                        fer1=6
                        fer2=10
                        fer3=2
                    if semilla == 'Platino':
                        fer1=6
                        fer2=10
                        fer3=5
                    if semilla == 'ASG':
                        fer1=6
                        fer2=10
                        fer3=8
                    if semilla == 'Centa':
                        fer1=6
                        fer2=10
                        fer3=11
                else:
                    if semilla == 'Oro Blanco':
                        fer1=0
                        fer2=1
                        fer3=2
                    if semilla == 'Platino':
                        fer1=3
                        fer2=4
                        fer3=5
                    if semilla == 'ASG':
                        fer1=6
                        fer2=7
                        fer3=8
                    if semilla == 'Centa':
                        fer1=9
                        fer2=10
                        fer3=11
    return (fer1,fer2,fer3)

