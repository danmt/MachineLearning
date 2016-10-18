import sys
import scipy.io
from clasificadores.MLP.RedNeuronal import RedNeuronal

def mlp3():
	red_neuronal = RedNeuronal("Perceptron",3,"Logistica")

	mat = scipy.io.loadmat('./pruebas/reglin.mat')
	
	X_entrenamiento = mat['x_train']
	y_entrenamiento = mat['y_train']

	# print(X_entrenamiento)
	# print(y_entrenamiento)

	X_test = mat['x_test']
	y_test = mat['y_test']

	red_neuronal.agregar_capa(1)
	red_neuronal.agregar_capa(2)
	red_neuronal.agregar_capa(1)

	#red_neuronal.imprimir_red()

	X = [[0.01,-0.45],[3,-0.45],[11,-0.65]]
	#X = [[0.01,-0.45]]
	y = [1,1,0]
	tasa = 0.01

	tieneSesgo = False
	epocas = 700

	print("Entrenamiento: ")
	
	red_neuronal.entrenar(X_entrenamiento,tieneSesgo,epocas,y_entrenamiento,tasa)

	# print("Validacion: ")
	
	# red_neuronal.entrenar(X_test,tieneSesgo,epocas,y_test,tasa)

	#red_neuronal.entrenar(X,tieneSesgo,epocas,y,tasa)

	#red_neuronal.imprimir_red()