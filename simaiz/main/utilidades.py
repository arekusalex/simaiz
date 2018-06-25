from .models import Departamento
import time

def buscar(listaSim, busqueda):
	sim_busqueda=list()
	for sim in listaSim:
		if busqueda in sim[0].nombre_sim.lower():
			sim_busqueda.append(sim)
			continue
		elif busqueda in sim[0].planta.nombre_planta.lower():
			sim_busqueda.append(sim)
			continue
		else:
			for fer in sim[1]:
				if busqueda in fer.nombre_fertilizante.lower():
					sim_busqueda.append(sim)
					break
			continue
	return sim_busqueda

def agregarDeptosDB():
	departamentos=['Ahuachapan','Santa Ana','Sonsonate','Chalatenango','La Libertad','San Salvador','La Paz',
		'San Vicente','Cuscatlan',"Cabañas", 'Usulutan', 'San Miguel','Morazan','La Union']
	deptos=Departamento.objects.all()
	if len(deptos)!=14:
		for depto in departamentos:
			d=Departamento(nombre_depto=depto)
			d.save()
	return

def tiempo_pagina(op):
	if op==0: #si es cero comienza el conteo
		global t_inicio
		t_inicio = time.time()
		return
	elif op==1: #si es uno detiene y devuelve el conteo
		sec=time.time()-t_inicio
		return round(sec,4)		
	else:
		print ('Parametro incorrecto')
		return