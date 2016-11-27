import numpy as np

def centros():
	centros = [
		np.array([-3.9]),
		np.array([-3.2]),
		np.array([-2.6]),
		np.array([-1.2]),
		np.array([-0.3]),
		np.array([0.1]),
		np.array([1.4]),
		np.array([2]),
		np.array([3.4]),
		np.array([3.95])
	]

	return centros

def anchuras():
	anchuras = [0.2,0.2,0.2,0.2,0.2,0.3,0.2,0.2,0.2,0.2]

	return anchuras

def pesos():
	pesos = [
		[0.8],
		[0.8],
		[1],
		[1],
		[1],
		[0.8],
		[0.8],
		[0.8],
		[0.8],
		[0.8]
	]

	return pesos

def sesgos():
	sesgos = [0.01]

	return sesgos


def tam_entrada():
	return 1

def tam_oculta():
	return 10

def tam_salida():
	return 1