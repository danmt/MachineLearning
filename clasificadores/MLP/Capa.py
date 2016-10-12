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
		for neurona_ant in ant.neuronas:
			neurona_ant.agregar_sinapsis(neuron,pos,peso)

	def iniciar_neuronas(self,tam,ant):
		peso = 0.1

		for x in xrange(0,tam):
			neurona = Neurona(x,self.activacion)
			self.neuronas[x] = neurona

			if ant != None:
				self.iniciar_sinapsis(x,ant,neurona,peso)

	def agregar_sig(self,capa_nueva):
		self.sig = capa_nueva
		self.esUltima = False

	def asignar_capa_entrada(self,entrada):
		for index, neurona in enumerate(self.neuronas):
			neurona.asignar_peso(entrada[index + 1])	

	def expansion(self):
		for neurona in self.neuronas:
			x = []
			w = []

			for neurona_interior in self.ant.neuronas:
				x.append(neurona_interior.peso)
				for sinapsis in neurona_interior.sinapsis:
					if sinapsis.llegada == neurona:
						w.append(sinapsis.peso)

			suma = comb_lineal(x,w)
			#funcion de activacion
			y = self.activacion(suma)

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


