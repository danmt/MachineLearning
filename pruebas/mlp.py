import sys
from clasificadores.MLP.RedNeuronal import RedNeuronal

def mlp3():
	red_neuronal = RedNeuronal("Perceptron",3,"Logistica")

	red_neuronal.agregar_capa(2)
	red_neuronal.agregar_capa(3)
	red_neuronal.agregar_capa(2)

	red_neuronal.imprimir_red()

	X = [[0.01,-0.45],[0.03,-0.55],[0.02,-0.65]]
	#X = [[0.01,-0.45]]
	y = [1,1,0]
	tasa = 0.5

	tieneSesgo = False
	epocas = 10000

	red_neuronal.entrenar(X,tieneSesgo,epocas,y,tasa)

	red_neuronal.imprimir_red()