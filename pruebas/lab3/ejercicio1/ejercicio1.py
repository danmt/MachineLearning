import sys
import scipy.io
from arquitecturas.MLP.RedNeuronal import RedNeuronal
from arquitecturas.MLP.Retropropagacion import entrenar
import matplotlib.pyplot as plt
import numpy as np

def init():
	red_neuronal = RedNeuronal("Perceptron",3,"Logistica")

	mat = scipy.io.loadmat('./pruebas/ejercicio1/datos/lab3/reglin.mat')
	
	X_entrenamiento = mat['x_train']
	y_entrenamiento = mat['y_train']

	# print(y_entrenamiento)

	X_test = mat['x_test']
	y_test = mat['y_test']

	red_neuronal.agregar_capa_entrada(1)
	red_neuronal.agregar_capa(8)
	red_neuronal.agregar_capa(1)

	def f(x,deriv=False):
		if deriv:
			return 1
		return x

	red_neuronal.capas[-1].cambiar_activacion(f)


	X = [[0.5]]
	#X = [[0.01,-0.45]]
	y = [[2]]
	tasa = 0.01

	tieneSesgo = True
	epocas = 700

	# red_neuronal.imprimir_red()

	# entrenar(red_neuronal,X,tieneSesgo,epocas,y,tasa)

	# red_neuronal.imprimir_red()

	red_neuronal.imprimir_red()
		
	plt.plot(X_test,y_test)
	
	entrenar(red_neuronal,X_entrenamiento,tieneSesgo,epocas,y_entrenamiento,tasa)

	x_in = np.array([])
	y_out = np.array([])

	red_neuronal.imprimir_red()

	for xi in X_test:
		x_in = np.append(x_in,xi)

		y = red_neuronal.calcular(xi)
		y_out = np.append(y_out,y)
	
	plt.plot(x_in,y_out,'-r')

	plt.show()