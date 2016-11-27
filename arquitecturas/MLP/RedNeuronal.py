from Capa import Capa
import time
from utilidades.Matematica import sigmoide, error_cuadratico_medio
import numpy as np
import matplotlib.pyplot as plt

class RedNeuronal:
	def __init__(self,tipo,capas,activation):
		self.tipo = tipo
		self.capas = []
		self.size = capas
		self.error_cometido = 1

		if (activation == 'Logistica'):
			self.activacion = sigmoide

	def agregar_capa_entrada(self,neuronas):
		capa_ant = None
		capa_nueva = None

		esPrimera = True
		esUltima = True

		cant_capas = 0

		capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)

		self.capas.append(capa_nueva)
		return True

	def agregar_capa(self,neuronas):
		cant_capas = len(self.capas)
		capa_ant = None
		capa_nueva = None

		esPrimera = False
		esUltima = True

		capa_ant = self.capas[cant_capas - 1]



		capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)


		capa_ant.agregar_sig(capa_nueva)

		self.capas[cant_capas - 1] = capa_ant
		self.capas.append(capa_nueva)

		return True

	##	Predecir				
	##	Precondicion.
	##	X : Vector de entrada	

	def predecir(self,X,y):
		errores = []
		y_total = []

		#print(y)

		for i,xi in enumerate(X):
			self.expansion(xi)
			yi = self.obtener_salida()

			y_total.append(yi)
			# if i % 1000 == 0:
			# 	print(error)

			error = y[i] - yi
			error = np.sum(error)

			#if error > 0:
			errores.append(error)

		self.error_cometido = error_cuadratico_medio(errores)
		#print(self.error_cometido)
		return y_total

	##	Predecir				
	##	Precondicion.
	##	X : Vector de entrada	

	def calcular(self,X):	
		capa = self.capas[0]

		capa.asignar_capa_entrada(X)

		X = np.insert(X,0,1)

		capa = capa.sig

		while capa != None:
			if capa.numero > 1:
				X = capa.ant.obtener_neuronas_pesadas()
				X = np.insert(X,0,1)
				
			for neurona in capa.neuronas:
				w = neurona.obtener_incidentes_sesgado()

				V = np.dot(X,w)

				fi = neurona.activacion(V)

				neurona.asignar_peso(fi)

			capa = capa.sig

		return self.obtener_salida()


	##	Predecir				
	##	Precondicion.
	##	X : Vector de entrada	

	def expansion(self,X):
		capa = self.capas[0]

		while not capa == None:
			if capa.numero == 0:
				#print(capa.neuronas)
				capa.asignar_capa_entrada(X)
			else:
				capa.expansion()
			
			capa = capa.sig

	def obtener_salida(self):
		capa = self.capas[-1]
		return capa.obtener_neuronas_pesadas()

	def imprimir_detalles(self):
		print("Tipo de red")
		print(self.tipo)
		print("Funcion de activacion")
		print(self.activation)

	def imprimir_red(self):
		print("Red Neuronal: ")

		for capa in self.capas:
			capa.imprimir_capa()
