from Sinapsis import Sinapsis
from Centro import Centro
import numpy as np
from utilidades.Matematica import gaussiana, identidad, distancia, comb_lineal

class Neurona_oculta:
	def __init__(self,funcion,dim_centro):
		self.valor = 0
		self.dim_centro = dim_centro
		#self.centro = [None] * dim_centro
		self.centro = Centro(dim_centro)

		self.asignar_funcion(funcion)

	def asignar_funcion(self,funcion):
		self.tipo_funcion = funcion

		if (funcion == 'gauss'):
			self.funcion = gaussiana
		else:
			print("funcion desconocida")


	def asignar_centro(self,coord,valor):
		self.centro.asignar_coordenada(coord,valor)

	def asignar_anchura(self,anchura):
		self.anchura = anchura

	def asignar_valor(self,valor):
		self.valor = valor

	def calcular(self,entrada):
		dist = distancia(entrada,self.centro.vector)

		self.valor = self.funcion(dist,self.anchura)
		return self.valor

class Neurona_salida:
	def __init__(self,funcion,cant_pesos):
		self.valor = 0
		self.funcion = funcion
		self.cant_pesos = cant_pesos
		self.pesos = [None] * cant_pesos

		self.asignar_funcion(funcion)

	def asignar_funcion(self,funcion):
		self.tipo_funcion = funcion

		if (funcion == 'ident'):
			self.funcion = identidad
		else:
			print("funcion desconocida")

	def asignar_sesgo(self,sesgo):
		self.sesgo = sesgo

	def asignar_peso(self,neurona,peso):
		self.pesos[neurona] = peso

	def asignar_valor(self,valor):
		self.valor = valor

	def calcular(self,capa_oculta):
		X = []

		for j, neurona_oculta in enumerate(capa_oculta):
			X.append(neurona_oculta.valor)

		self.valor = comb_lineal(X,self.pesos) + self.sesgo