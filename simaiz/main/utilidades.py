
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