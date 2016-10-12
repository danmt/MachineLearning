import matplotlib.pyplot as plt
import numpy as np
import time
from Utilidades import comb_lineal

def plot_points(x,d):
	for i, point in enumerate(x):
		x1 = x[i][1:][0]
		x2 = x[i][1:][1]
		y = d[i]

		marker = 'ro'

		if (y == 0):
			marker = 'g^'

		plt.plot(x1,x2,marker)

def signo(val):
	if val > 0:
		return 1

	return -1

def error_clasif(d,y):
	return d - y

class Perceptron:
	def __init__(self,epocas,eta):
		self.epocas = epocas
		self.eta = eta

	def train(self,x,d,w):
		weigths = [w,w,w]

		plt.axis([-10, 10, -10, 10])
		
		plot_points(x,d)

		for epoca in xrange(0,self.epocas):
			size = len(x)
			errors = [0] * size

			print("Epoca #" + str(epoca))

			for i in xrange(0,size):
				suma = comb_lineal(x[i],weigths)
				y = signo(suma)
				errors[i] = error_clasif(d[i][0],y)

				#print(errors[i])

				if errors[i] != 0:
					weigths[0] = weigths[0] + self.eta * errors[i]
					weigths[1] = weigths[1] + self.eta * errors[i] * x[i][1]
					weigths[2] = weigths[2] + self.eta * errors[i] * x[i][2]
			
		Wa = weigths[0]/weigths[2]
		Wb = weigths[1]/weigths[2]

		#print(Wa)
		#print(Wb)

		def test(x):
			return -Wa-Wb*x

		values = np.array(range(-1,1))

		plt.plot(values,test(values))

		plt.show()

