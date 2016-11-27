from utilidades.Matematica import sigmoide, comb_lineal, error_cuadratico_medio
import numpy as np
import matplotlib.pyplot as plt


def agregar_sesgo(X):
	#Agregamos el sesgo
	b = np.atleast_2d(np.ones(X.shape[0]))

	#Concatenamos vector de 1's
	X = np.concatenate((b.T,X),axis=1)

	return X

def calculo_theta(neurona,capa,activacion,y):	
	w = neurona.obtener_pesos()
	y = capa.sig.obtener_neuronas_pesadas()
	V = comb_lineal(y,w)

	return activacion(V,True)

def calculo_error_capa_salida(esperado,salida):
	#print(esperado)
	#print(esperado-salida)
	return esperado - salida

def calculo_error_capa_oculta(neurona):
	gradientes = neurona.capa.sig.obtener_neuronas_gradiente()
	pesos = neurona.obtener_pesos()
	
	return comb_lineal(gradientes,pesos)

def calculo_incidencias(neurona):
	pesos = neurona.obtener_incidentes_sesgado()
	neuronas = np.array([1.])

	for neuron in neurona.capa.ant.neuronas:
		neuronas = np.append(neuronas,neuron.peso)

	return comb_lineal(neuronas,pesos)


def entrenar(red,X,tieneSesgo,epocas,y,tasa):
	X = np.array(X)
	y = np.array(y)

	errores = []

	if not tieneSesgo:
		X = agregar_sesgo(X)

	for i in range(epocas):
		#print(X)
		retropropagacion(red,X,y,tasa)

		errores.append(red.error_cometido)

	# plt.axis([0,1000,0,6])
	# plt.plot(errores)
	# plt.show()	

def retropropagacion(red,X,y,tasa):
	errores = [1]

	#print(red.capas)

	for i,xi in enumerate(X):
		#print(xi)
		red.calcular(xi)
		#print(red.obtener_salida())
		#expansion(red,xi)
		calculo_gradientes(red,xi,y[i])
		actualizar_pesos(red,tasa)

		yi = red.obtener_salida()

		#if (i % 50 == 0):
		# print("x="),
		# print(xi)
		# print("y="),
		# print(yi)
		#red.imprimir_red()

		# yi = red.calcular(xi)
		# error = y[i] - yi

		
		# errores.append(error[0])

	#print(errores)
	red.error_cometido = error_cuadratico_medio(errores)
	#print(red.error_cometido)

##	Expansion				
##	Precondicion.
##	X : Vector de entrada	

def expansion(red,X):
	capa = red.capas[0]

	while not capa == None:
		if capa.numero == 0:
			capa.asignar_capa_entrada(X)
		else:
			capa.expansion()
		
		capa = capa.sig

##	Calculo del gradiente				
##	Precondicion.
##	X : Vector de entrada
##	y : Vector de salida esperada	

def calculo_gradientes(red,X,y):
	capa = red.capas[-1]

	while not capa.ant == None:
		for i,neurona in enumerate(capa.neuronas):
			V = calculo_incidencias(neurona)

			theta = neurona.activacion(V,True)

			if capa.esUltima:
				error = calculo_error_capa_salida(y[i],neurona.peso)
			else:
				error = calculo_error_capa_oculta(neurona)

			neurona.gradiente = theta * error
			#print(neurona.gradiente)
		
		capa = capa.ant

##	Actualizar pesos				
##	Precondicion.
##	X : Vector de entrada
##	y : Vector de salida esperada	

def actualizar_pesos(red,tasa):
	capa = red.capas[-2]

	while not capa == None:
		for i,neurona in enumerate(capa.neuronas):

			for sinapsis in neurona.sinapsis:
				sinapsis.peso += tasa * sinapsis.llegada.gradiente * neurona.peso
				sinapsis.llegada.sesgo += tasa * sinapsis.llegada.gradiente
					
				
				#sinapsis.actualizar_peso(peso)
			
		capa = capa.ant
