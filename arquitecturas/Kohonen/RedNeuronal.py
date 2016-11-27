from Malla import Malla

from aprendizaje import vecindad_fn, tasa_aprendizaje_fn


class RedNeuronal:
	def __init__(self,dimension_entrada,tam,cant_clases):
		self.dimension_entrada = dimension_entrada
		self.tam = tam

		self.malla = Malla(dimension_entrada,tam,cant_clases)

	# Se halla el nodo mas cercano y se actualiza su peso
	def entrenar(self,entradas,salidas,tasa_aprendizaje_ini,epocas):
		for iteracion in xrange(0,epocas):
			for i, entrada in enumerate(entradas):
				vecindad = vecindad_fn(self.tam,iteracion,epocas)
				tasa_aprendizaje = tasa_aprendizaje_fn(tasa_aprendizaje_ini,iteracion,epocas)

				self.malla.entrenar_malla(entrada,salidas[i],vecindad,tasa_aprendizaje)	

	def obtener_mapa(self):
		self.malla.calcular_mapa()
		self.malla.imprimir_mapa()