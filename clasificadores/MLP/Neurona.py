from Sinapsis import Sinapsis

class Neurona:
	def __init__(self,pos,activationFn):
		self.peso = 0
		self.pos = pos
		self.sinapsis = []
		self.activationFn = activationFn

	def agregar_sinapsis(self,llegada,pos,peso):
		sinapsis = Sinapsis(llegada,peso)
		self.sinapsis.append(sinapsis)

	def asignar_peso(self,peso):
		self.peso = peso

	def activate(self):
		print("Se ejecuta la funcion de activacion")
		print(self.activationFn(0.458))

	def imprimir_detalles(self):
		spacing = "  " + "  "

		print(spacing + "Neurona nro " + str(self.pos) + ", con acumulado " + str(self.peso))

	def imprimir_neurona(self):
		spacing = "  "

		neuronaMsj = "Neurona #" + str(self.pos) + " de peso " + str(self.peso)

		if len(self.sinapsis) > 0:
			neuronaMsj = neuronaMsj + " posee las siguientes sinapsis:"

		print(spacing + neuronaMsj)

		for sinapsis in self.sinapsis:
			print(spacing + spacing + "W[" + str(self.pos) + "," + str(sinapsis.llegada.pos) + "] = " + str(sinapsis.peso))
			#sinapsis.imprimir_sinapsis()