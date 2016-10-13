import numpy as np

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
	return (0.5)*np.sum(np.exp2(errores))