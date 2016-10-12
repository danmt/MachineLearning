from Capa import Capa
from scipy.special import expit
import time

class RedNeuronal:
	def __init__(self,tipo,capas,activation):
		self.tipo = tipo
		self.capas = []
		self.size = capas

		if (activation == 'Logistica'):
			self.activacion = expit

	def agregar_capa(self,neuronas):
		cant_capas = len(self.capas)
		capa_ant = None
		capa_nueva = None

		esPrimera = True
		esUltima = True

		if cant_capas == 0:
			capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)
			self.capas.append(capa_nueva)
			return True

		capa_ant = self.capas[cant_capas - 1]
		esPrimera = False

		capa_nueva = Capa(cant_capas,neuronas,esPrimera,esUltima,self.activacion,capa_ant)

		capa_ant.agregar_sig(capa_nueva)

		self.capas[cant_capas - 1] = capa_ant
		self.capas.append(capa_nueva)

		return True

	def entrenar(self):
		data = [1,0.01,-0.45]

		self.expansion(data)
		#retropropagacion con calculo de gradiente local
		#actualizacion de pesos
	
	def expansion(self,entrada):
		capa = self.capas[0]

		while not capa == None:
			if capa.numero == 0:
				capa.asignar_capa_entrada(entrada)
			else:
				capa.expansion()
			
			capa = capa.sig

	def imprimir_detalles(self):
		print("Tipo de red")
		print(self.tipo)
		print("Funcion de activacion")
		print(self.activation)

	def imprimir_red(self):
		print("Red Neuronal: ")

		for capa in self.capas:
			capa.imprimir_capa()
