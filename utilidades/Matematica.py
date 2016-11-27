import numpy as np
from math import sqrt, exp

def comb_lineal(x,w):
	suma = 0

	for i, xi in enumerate(x):
		suma = suma + (xi * w[i])

	return suma

def sigmoide(x,deriv=False):
	if deriv:
		return sigmoide(x)*(1-sigmoide(x))
	return 1.0/(1.0 + np.exp(-x))

def error_cuadratico_medio(errores):
	rounded = 1 / float(len(errores))
	return (rounded)*np.sum(np.exp2(errores))

def gaussiana(r,sigma):
	x = - (r**2) / (2*(sigma**2))
	return exp(x)

def identidad(x):
	return x

def distancia(x,y):
	suma = 0

	for i, val in enumerate(x):
		nuevo_val = x[i] - y[i]
		nuevo_val = nuevo_val * nuevo_val

		suma += nuevo_val

	return sqrt(suma)