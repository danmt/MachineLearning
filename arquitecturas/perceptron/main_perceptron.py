import sys
from NeuralNetwork import NeuralNetwork
import scipy.io
from Perceptron import Perceptron


def main():
	mat = scipy.io.loadmat('lincloud3.mat')

	X = mat['X']
	d = mat['d']
	w = 0.1
	epocas = 400
	tasa_aprendizaje = 0.5

	perceptron = Perceptron(epocas,tasa_aprendizaje)

	perceptron.train(X,d,w)

if __name__ == '__main__':
	main()
