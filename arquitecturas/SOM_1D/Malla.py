import numpy as np
from Neurona import Neurona
from utilidades.Matematica import distancia

class Malla:
	def __init__(self,dimension_entrada,tam):
		self.tam = tam
		self.vector = [None] * tam

		self.generarMalla(dimension_entrada,tam)

	def generarMalla(self,dimension_entrada,tam):
		for index, x in enumerate(self.vector):
			self.vector[index] = Neurona(dimension_entrada)

	def hallar_mejor_candidato(self,entrada):
		mejor_candidato = None

		for candidato in self.vector:
			dist = distancia(entrada,candidato.pesos)

			if not mejor_candidato:
				mejor_candidato = candidato
				mejor_distancia = dist
				continue

			if dist < mejor_distancia:
				mejor_distancia = dist
				mejor_candidato = candidato

		return mejor_candidato


