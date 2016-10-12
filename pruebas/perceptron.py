import scipy.io
from clasificadores.perceptron.Perceptron import Perceptron

def perceptron3():
	mat = scipy.io.loadmat('./clasificadores/perceptron/lincloud3.mat')

	X = mat['X']
	d = mat['d']
	w = 0.1
	epocas = 400
	tasa_aprendizaje = 0.5

	perceptron = Perceptron(epocas,tasa_aprendizaje)

	perceptron.train(X,d,w)