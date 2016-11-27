from Malla import Malla

class RedNeuronal:
	def __init__(self,dimension_entrada,tam):
		self.dimension_entrada = dimension_entrada

		self.malla = Malla(dimension_entrada,tam)

	# Hallar nodo mas cercano en distancia euclidea
	def hallar_mejor_candidato(self,entrada):
		return self.malla.hallar_mejor_candidato(entrada)

	# Se halla el nodo mas cercano y se actualiza su peso
	def entrenar(self,entradas,tasa_aprendizaje,epocas):
		for entrada in entradas:
			mejor_candidato = self.hallar_mejor_candidato(entrada)

			actualizacion_peso = entrada - mejor_candidato.pesos

			actualizacion_peso *= tasa_aprendizaje

			mejor_candidato.pesos += actualizacion_peso

	# Se retornan los centros
	def obtener_centros(self):
		centros = []

		for nodo in self.malla.vector:
			centros.append(nodo.pesos)

		return centros