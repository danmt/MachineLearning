from Neurona import Neurona_oculta, Neurona_salida
from Capa import Capa_oculta, Capa_salida

import time
import matplotlib.pyplot as plt
from scipy import zeros

class RedNeuronal:
	def __init__(self,cant_entrada,cant_ocultas,cant_salida,funcion_oculta,funcion_salida):
		self.cant_entrada = cant_entrada
		self.cant_ocultas = cant_ocultas
		self.cant_salida = cant_salida

		self.capa_entrada = [None] * cant_entrada
		
		self.agregar_capa_oculta(cant_ocultas,funcion_oculta)
		self.agregar_capa_salida(cant_salida,funcion_salida)

	def agregar_capa_entrada(self,entrada):
		if (len(entrada) != len(self.capa_entrada)):
			print("Error: dimensionalidad de entrada incorrecta.")
			return False

		for index, coordenada in enumerate(entrada):
			self.capa_entrada[index] = coordenada

		return True

	def agregar_capa_oculta(self,cant_ocultas,funcion_oculta):
		self.capa_oculta = Capa_oculta(cant_ocultas,funcion_oculta)
		self.capa_oculta.asignar(self.cant_entrada)

		return True

	def agregar_capa_salida(self,cant_salida,funcion_salida):	
		self.capa_salida = Capa_salida(cant_salida,funcion_salida)
		self.capa_salida.asignar(self.cant_ocultas)

		return True

	def asignar_pesos(self,pesos):
		self.capa_salida.asignar_pesos(pesos)

		return True
	
	def asignar_sesgos(self,sesgos):
		self.capa_salida.asignar_sesgos(sesgos)

		return True

	def asignar_centros(self,centros):
		self.capa_oculta.asignar_centros(centros)
				
		return True

	def asignar_anchuras(self,anchuras):
		self.capa_oculta.asignar_anchuras(anchuras)
				
		return True


	def calcular(self,entrada):
		self.agregar_capa_entrada(entrada)

		self.capa_oculta.calcular(entrada)

		self.capa_salida.calcular(self.capa_oculta.neuronas)

	def graficar_salida(self,entrada,figure):
		salida = []

		for xi in entrada:
			self.calcular([xi])
			yi = self.capa_salida.neuronas[0].valor
			salida.append([yi])

		figure.plot(entrada, salida, 'r-', linewidth=2)

	def graficar_centros(self,figure):
		centros = []
		ceros = zeros(len(self.capa_oculta.neuronas))

		for index, neurona in enumerate(self.capa_oculta.neuronas):
			centros.append(neurona.centro.vector)

		figure.plot(centros,ceros,'gs')

	def graficar_funciones(self,entrada,figure):
		for index, neurona in enumerate(self.capa_oculta.neuronas):
			salida = []

			for xi in entrada:
				# self.calcular([xi])
				# yi = self.capa_salida.neuronas[0].valor
				
				#neurona.calcular([xi])
				resulFn = neurona.calcular([xi])
				peso = self.capa_salida.neuronas[0].pesos[index]

				salida.append(resulFn*peso)

				# print("centro= "),
				# print(neurona.centro)
				# print("salida= "),
				# print(yi)


			figure.plot(entrada,salida,'k-')


	def imprimir(self):
		print("Entrada")

		print("Oculta")

		for i, neurona_oculta in enumerate(self.capa_oculta):
			print("Centro: "),
			print(neurona_oculta.centro)

			print("Anchura: "),
			print(neurona_oculta.anchura)

			print("Valor: "),
			print(neurona_oculta.valor)

		print("Salida")

		for i, neurona_salida in enumerate(self.capa_salida):
			print("Pesos: "),
			print(neurona_salida.pesos)

			print("Sesgo: "),
			print(neurona_salida.sesgo)

			print("Valor: "),
			print(neurona_salida.valor)