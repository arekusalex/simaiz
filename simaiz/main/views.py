from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
	return render(request, "main/index.html", {})

@login_required()
def direccionar(request):
	if request.user.is_authenticated:
		return redirect('mi_espacio', username=request.user.username)
	else:
		return redirect('main_inicio') 

		
@login_required()
def mi_espacio(request, username):
	if username == request.user.username:
		contexto = {
		'nombre': request.user.first_name+' '+request.user.last_name,
		}
		return render(request, "main/mi_espacio.html", contexto)
	else:
		return redirect('mi_espacio', username=request.user.username)
