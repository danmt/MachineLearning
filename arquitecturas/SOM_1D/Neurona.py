import numpy as np

class Neurona:
	def __init__(self,dimension_entrada):
		self.dimension_entrada = dimension_entrada
		self.pesos = np.random.normal(0, 1, dimension_entrada)