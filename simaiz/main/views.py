from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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

def direccionar(request):
	return redirect('mi_espacio',username=request.user.username)


@login_required()
def mi_espacio(request,username):
	contexto={
		'nombre':request.user.first_name+' '+request.user.last_name,
	}
	return render(request, "main/mi_espacio.html", contexto)
