from Sinapsis import Sinapsis
import numpy as np

class Neurona:
	def __init__(self,capa,pos,activacion):
		self.peso = 0
		self.pos = pos
		self.sinapsis = []
		self.activacion = activacion
		self.capa = capa
		self.gradiente = 0
		self.sesgo = 0

	def agregar_sinapsis(self,llegada,pos,peso):
		sinapsis = Sinapsis(llegada,peso)
		self.sinapsis.append(sinapsis)

	def obtener_pesos(self):
		sinapsis = []

		for sinap in self.sinapsis:
			sinapsis.append(sinap.peso)

		return sinapsis

	def asignar_peso(self,peso):
		self.peso = peso

	def obtener_incidentes_sesgado(self):
		incidentes = np.array([1.])

		capa_ant = self.capa.ant

		if capa_ant == None:
			return incidentes

		for neurona in capa_ant.neuronas:
			for sinapsis in neurona.sinapsis:
				if self == sinapsis.llegada:
					incidentes = np.append(incidentes,float(sinapsis.peso))

		return incidentes


	def obtener_incidentes(self):
		incidentes = []
		capa_ant = self.capa.ant

		if capa_ant == None:
			return incidentes

		for neurona in capa_ant.neuronas:
			for sinapsis in neurona.sinapsis:
				if self == sinapsis.llegada:
					incidentes.append(sinapsis.peso)

		return incidentes

	def activate(self):
		print("Se ejecuta la funcion de activacion")
		print(self.activacion(0.458))

	def imprimir_detalles(self):
		spacing = "  " + "  "

		print(spacing + "Neurona nro " + str(self.pos) + ", con acumulado " + str(self.peso))

	def imprimir_neurona(self):
		spacing = "  "

		neuronaMsj = "Neurona #" + str(self.pos) + " de peso " + str(self.peso)

		neuronaMsj = neuronaMsj + " y gradiente " + str(self.gradiente) + "\n"

		neuronaMsj = neuronaMsj + " con sesgo b = " + str(self.sesgo) + "\n"

		if len(self.sinapsis) > 0:
			neuronaMsj = neuronaMsj + "   Posee las siguientes sinapsis:"

		print(spacing + neuronaMsj)

		for sinapsis in self.sinapsis:
			print(spacing + spacing + "W[" + str(self.pos) + "," + str(sinapsis.llegada.pos) + "] = " + str(sinapsis.peso))
			#sinapsis.imprimir_sinapsis()