from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicioConfig(request):
	return render(request,"configuracion/configuracion.html")