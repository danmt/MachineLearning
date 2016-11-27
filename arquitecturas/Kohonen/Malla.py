import numpy as np
from Neurona import Neurona
from utilidades.Matematica import distancia
from aprendizaje import dist_pitagoras, influencia_fn
import sys

class Malla:
	def __init__(self,dimension_entrada,tam,cant_clases):
		self.tam = tam

		self.generar_malla(dimension_entrada,cant_clases)

	def generar_malla(self,dimension_entrada,cant_clases):
		M = []

		for i in xrange(0,self.tam):
			X = []
			
			for j in xrange(0,self.tam):
				X.append(Neurona(dimension_entrada,cant_clases,i,j))

			M.append(X)

		self.matriz = M

	def entrenar_malla(self,entrada,salida,vecindad,tasa_aprendizaje):
		mejor_candidato = self.hallar_mejor_candidato(entrada)

		for i in xrange(0,self.tam):
			for j in xrange(0,self.tam):
				dist = dist_pitagoras(mejor_candidato.x,mejor_candidato.y,i,j)

				if dist <= vecindad:
					influencia = influencia_fn(dist,vecindad);
					self.matriz[i][j].actualizar_pesos(entrada,salida,influencia,tasa_aprendizaje)

	def hallar_mejor_candidato(self,entrada):
		mejor_candidato = None
		mejor_distancia = sys.maxint

		for i in xrange(0,self.tam):
			for j in xrange(0,self.tam):
				candidato = self.matriz[i][j]
				dist = distancia(entrada,candidato.pesos)

				if dist < mejor_distancia:
					mejor_distancia = dist
					mejor_candidato = candidato

		return mejor_candidato

	def calcular_mapa(self):
		for i in xrange(0,self.tam):
			for j in xrange(0,self.tam):
				self.matriz[i][j].actualizar_ganadora()

	def imprimir_mapa(self):
		for i in xrange(0,self.tam):
			print("[" + str(i) + "]"),

			for j in xrange(0,self.tam):
				print(self.matriz[i][j].clase_ganadora),
			print("")
					