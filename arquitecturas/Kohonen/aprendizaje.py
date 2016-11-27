from math import fabs, exp, log

def vecindad_fn(tam,iteracion,epocas):
	radio_mapa = tam / 2

	constante_tiempo = epocas / log(radio_mapa)

	result = radio_mapa * exp(- iteracion / constante_tiempo)

	return result

def tasa_aprendizaje_fn(tasa_aprendizaje,iteracion,epocas):
	actualizacion = exp(- iteracion / epocas);
	result = tasa_aprendizaje * actualizacion
	return result

def dist_pitagoras(x1,y1,x2,y2):
	return fabs(x1 - x2) + fabs(y1 - y2)

def influencia_fn(dist,vecindad):
	return exp(- dist / (2*vecindad));