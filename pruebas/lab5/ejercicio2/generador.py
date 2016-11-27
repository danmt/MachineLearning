import numpy as np
import config

tam = config.tam()
cant = config.cant()

def gaussiana(clase,centro,varianza):
	valores = []

	for i in xrange(0,tam):
		valores.append(np.random.normal(centro[i],varianza,cant))

	X = []

	for i in xrange(0,cant):
		vector = []

		for j in xrange(0,tam):
			vector.append(valores[j][i])

		X.append(vector)

	return X


def datos():
	varianza = config.varianza()
	
	centros = config.centros()
	
	X = np.arange(0)
	Y = np.arange(0)

	for clase, centro in enumerate(centros):
		xi = gaussiana(clase,centro,varianza)
		yi = [clase] * cant

		if len(X) == 0 or len(Y) == 0:
			X = xi
			Y = yi
			continue

		X = np.concatenate((X,xi))
		Y = np.concatenate((Y,yi))

	return [X,Y]