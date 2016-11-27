import numpy as np

class Neurona:
	def __init__(self,dimension_entrada,cant_clases,x,y):
		self.dimension_entrada = dimension_entrada
		self.pesos = np.random.normal(0, 1, dimension_entrada)

		self.x = x
		self.y = y

		self.clases = dict()

		for x in xrange(-1,cant_clases):
			self.clases[x] = 0

		self.clase_ganadora = -1

	def actualizar_ganadora(self):
		minimo = 0

		clase_ganadora = self.clase_ganadora

		for clave in self.clases:
			valor = self.clases[clave] 
			
			if valor > minimo:
				minimo = valor
				clase_ganadora = clave

		self.clase_ganadora = clase_ganadora

	def actualizar_pesos(self,entrada,salida,influencia,tasa_aprendizaje):
		actualizacion_peso = entrada - self.pesos

		actualizacion_peso *= influencia * tasa_aprendizaje

		self.pesos += actualizacion_peso

		self.clases[salida] += 1