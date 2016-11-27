class Sinapsis:
	def __init__(self,llegada,peso):
		self.llegada = llegada
		self.peso = peso 

	def actualizar_peso(self,peso):
		self.peso = peso

	def print_synapse(self):
		spacing = "  " + "  "
		self.llegada.imprimir_detalles()
		print(spacing + "Peso de la conexion: " + str(self.peso))
