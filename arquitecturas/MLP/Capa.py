from Neurona import Neurona
from utilidades.Matematica import comb_lineal

class Capa:
	def __init__(self,numero,tam,esPrimera,esUltima,activacion,ant):
		self.numero = numero
		self.neuronas = [None] * tam
		self.tam = tam
		self.esUltima = esUltima
		self.esPrimera = esPrimera
		self.activacion = activacion
		self.ant = ant
		self.sig = None

		self.iniciar_neuronas(tam,ant)

	def iniciar_sinapsis(self,pos,ant,neuron,peso):
		neuron.sesgo = peso

		for neurona_ant in ant.neuronas:
			neurona_ant.agregar_sinapsis(neuron,pos,peso)

	def obtener_neuronas_pesadas(self):
		neuronas_pesadas = []

		for i,neurona in enumerate(self.neuronas):
			neuronas_pesadas.append(neurona.peso)

		return neuronas_pesadas

	def obtener_neuronas_gradiente(self):
		neuronas_gradiente = [None] * len(self.neuronas)

		for i,neurona in enumerate(self.neuronas):
			neuronas_gradiente[i] = neurona.gradiente

		return neuronas_gradiente

	def iniciar_neuronas(self,tam,ant):
		peso = 0.2

		for x in xrange(0,tam):
			neurona = Neurona(self,x,self.activacion)
			self.neuronas[x] = neurona

			if ant != None:
				self.iniciar_sinapsis(x,ant,neurona,peso)

	def agregar_sig(self,capa_nueva):
		self.sig = capa_nueva
		self.esUltima = False

	def asignar_capa_entrada(self,entrada):
		# print("entrada = "),
		# print(entrada)
		for index, neurona in enumerate(self.neuronas):
		#	print(index)
			neurona.asignar_peso(entrada[index])

	def cambiar_activacion(self,activacion):
		# print("entrada = "),
		# print(entrada)
		self.activacion = activacion
		for index, neurona in enumerate(self.neuronas):
			neurona.activacion = activacion
		#	print(index)

	def expansion(self):
		# print("Capa #"),
		# print(self.numero)

		for neurona in self.neuronas:
			x = []
			w = []

			for neurona_anterior in self.ant.neuronas:
				x.append(neurona_anterior.peso)
				for sinapsis in neurona_anterior.sinapsis:
					if sinapsis.llegada == neurona:
						w.append(sinapsis.peso)

			suma = comb_lineal(x,w)
			#funcion de activacion
			y = self.activacion(suma)

			# print("Neurona #"),
			# print(neurona.pos),

			# print(" peso "),
			# print(y)
			neurona.asignar_peso(y)

	def imprimir_capa(self):
		capaMsj = "\nCapa numero " + str(self.numero)

		if self.esPrimera:
			capaMsj = capaMsj + " entrada."
		elif self.esUltima:
			capaMsj = capaMsj + " salida."
		else:
			capaMsj = capaMsj + " oculta."

		print(capaMsj)

		spacing = "  " + "  "

		for index, neuron in enumerate(self.neuronas):		
			neuron.imprimir_neurona()


