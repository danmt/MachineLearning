import sys
import scipy.io
from arquitecturas.MLP.RedNeuronal import RedNeuronal
from arquitecturas.MLP.Retropropagacion import entrenar
import matplotlib.pyplot as plt
import numpy as np

def init():
	red_neuronal = RedNeuronal("Perceptron",3,"Logistica")

	mat = scipy.io.loadmat('./pruebas/lab3/ejercicio2/datos/rabbit.mat')
	
	red_neuronal.agregar_capa(1)
	red_neuronal.agregar_capa(1)
	red_neuronal.agregar_capa(1)

	X = mat['wgt']
	y = mat['age']

	tasa = 0.01

	tieneSesgo = False
	epocas = 300
	
	#Funcion dada en el problema
	def f(x):
		a = 233.846
		b = -0.00604

		#Logaritmo de un negativo?
		print(np.log(1 - x/a))

		return (1/b)*np.log(1 - (x/a))

	entrada = []
	salida = []

	for xi in X:
		entrada.append(xi[0])
		salida.append(f(xi[0]))

		
	plt.plot(entrada,salida)

	entrenar(red_neuronal,X,tieneSesgo,epocas,y,tasa)

	for xi in X:
		#Agregar Sesgo
		xi = np.insert(xi,0,1.)

	red_neuronal.imprimir_red()
	
	plt.show()

