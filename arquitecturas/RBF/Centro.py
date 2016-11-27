class Centro:
	def __init__(self,dimension):
		self.dimension = dimension
		self.vector = [None] * self.dimension

	def asignar_coordenada(self,coord,valor):
		self.vector[coord] = valor