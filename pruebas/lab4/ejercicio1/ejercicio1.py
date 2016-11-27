import sys
import scipy.io
from arquitecturas.RBF.RedNeuronal import RedNeuronal
from utilidades.Matematica import gaussiana
import matplotlib.pyplot as plt
import numpy as np
from scipy import *

def init():
	funcion_oculta = "gauss"
	funcion_salida = "ident"

	red_neuronal = RedNeuronal(1,12,1,funcion_oculta,funcion_salida)

	centros = [
		[50],
		[90],
		[150],
		[220],
		[250],
		[310],
		[380],
		[470],
		[610],
		[680],
		[720],
		[800]
	]

	anchuras = [20,20,32,35,20,30,50,40,60,40,30,40]

	pesos = [
		[60],
		[78],
		[110],
		[105],
		[100],
		[130],
		[190],
		[220],
		[240],
		[110],
		[130],
		[120]
	]

	sesgos = [0.1]

	#entrada = [1.0,-2.0,3.0]


	red_neuronal.asignar_pesos(pesos)
	red_neuronal.asignar_centros(centros)
	red_neuronal.asignar_sesgos(sesgos)
	red_neuronal.asignar_anchuras(anchuras)


	mat = scipy.io.loadmat('./pruebas/lab4/ejercicio1/datos/rabbit.mat')
	
	age = mat['age']
	wgt = mat['wgt']

	wgt2 = []

	#SE GRAFICAN LA ENTRADA
	plt.figure(figsize=(12, 8))
	plt.plot(age, wgt, 'bo')

	#DATOS DE VALIDACION
	entrada = xrange(1,1000)

	#SE GRAFICA LA SALIDA
	red_neuronal.graficar_salida(entrada)

	#SE GRAFICAN LOS CENTROS
	red_neuronal.graficar_centros()

	#SE GRAFICAN LAS FUNCIONES
	red_neuronal.graficar_funciones(entrada)


	plt.show()
	