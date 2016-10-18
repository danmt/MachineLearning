from Capa import Capa
from scipy.special import expit
import time
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
	return esperado - salida

def calculo_error_capa_oculta():
	return 1


class RedNeuronal:
	def __init__(self,tipo,capas,activation):
		self.tipo = tipo
		self.capas = []
		self.size = capas
		self.error_cuadratico_medio = 1

		if (activation == 'Logistica'):
			self.activacion = sigmoide

	def agregar_capa(self,neuronas):
		cant_capas = len(self.capas)
		capa_ant = None
		capa_nueva = None

		esPrimera = True
		esUltima = True

		if cant_capas == 0:
			capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)
			self.capas.append(capa_nueva)
			return True

		capa_ant = self.capas[cant_capas - 1]
		esPrimera = False

		capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)

		capa_ant.agregar_sig(capa_nueva)

		self.capas[cant_capas - 1] = capa_ant
		self.capas.append(capa_nueva)

		return True

	##	Entrenar.
	##	Precondicion.
	##	X : Vector de entrada
	##	y : Vector de salida esperada
	##  tieneSesgo: Booleano. True si la entrada tiene sesgo
	##	epocas : Cantidad de veces que correra el algoritmo

	def entrenar(self,X,tieneSesgo,epocas,y,tasa):
		X = np.array(X)
		y = np.array(y)
		errores = []

		if not tieneSesgo:
			X = agregar_sesgo(X)

		for i in range(epocas):
			self.retroprogagacion(X,y,tasa)

			# print("error_cuadratico_medio: "),
			# print(self.error_cuadratico_medio)

			if i % 50 == 0:
				print(self.error_cuadratico_medio)

			errores.append(self.error_cuadratico_medio)
			
		plt.axis([0,1000,0,6])
		plt.plot(errores)
		plt.show()
		
	##	Retropropagacion				
	##	Precondicion.
	##	X : Vector de entrada
	##	y : Vector de salida esperada

	def retroprogagacion(self,X,y,tasa):
		for i,xi in enumerate(X):
			self.expansion(xi)
			self.calculo_gradientes(xi,y)
			self.actualizar_pesos(tasa)

	##	Expansion				
	##	Precondicion.
	##	X : Vector de entrada	

	def expansion(self,X):
		capa = self.capas[0]

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

	def calculo_gradientes(self,X,y):
		capa = self.capas[len(self.capas) - 1]

		while not capa.ant == None:
			if capa.esUltima:
				errores = []

			for i,neurona in enumerate(capa.neuronas):
				if capa.esUltima:
					theta = self.activacion(y[i],True)
					error = y[i] - neurona.peso

					errores.append(error)
				else:
					theta = calculo_theta(neurona,capa,self.activacion,y)
					gradientes = neurona.capa.sig.obtener_neuronas_gradiente()
				 	pesos = neurona.obtener_pesos()

					error = comb_lineal(gradientes,pesos)

				neurona.gradiente = theta * error
			
			if capa.esUltima:
				self.error_cuadratico_medio = error_cuadratico_medio(errores)
			
			capa = capa.ant

	##	Actualizar pesos				
	##	Precondicion.
	##	X : Vector de entrada
	##	y : Vector de salida esperada	

	def actualizar_pesos(self,tasa):
		capa = self.capas[len(self.capas) - 2]

		while not capa == None:
			for i,neurona in enumerate(capa.neuronas):
				for sinapsis in neurona.sinapsis:
					cambio = tasa * sinapsis.llegada.gradiente * neurona.peso
					peso = sinapsis.peso + cambio
					
					sinapsis.actualizar_peso(peso)
				
			capa = capa.ant

	

	def imprimir_detalles(self):
		print("Tipo de red")
		print(self.tipo)
		print("Funcion de activacion")
		print(self.activation)

	def imprimir_red(self):
		print("Red Neuronal: ")

		for capa in self.capas:
			capa.imprimir_capa()
