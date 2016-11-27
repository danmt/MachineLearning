import sys
import scipy.io
from arquitecturas.Kohonen.RedNeuronal import RedNeuronal as Kohonen
from utilidades.Matematica import gaussiana
import matplotlib.pyplot as plt
import numpy as np
from scipy import *
import generador

def init():
	datos = generador.datos()

	x = datos[0]
	y = datos[1]

	kohonen = Kohonen(8,10,4)

	kohonen.entrenar(x,y,0.05,10)

	kohonen.obtener_mapa()


	