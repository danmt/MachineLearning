import sys
from RedNeuronal import RedNeuronal

def main():
	red_neuronal = RedNeuronal("Perceptron",3,"Logistica")

	red_neuronal.agregar_capa(2)
	red_neuronal.agregar_capa(3)
	red_neuronal.agregar_capa(2)

	red_neuronal.imprimir_red()

	red_neuronal.entrenar()

	red_neuronal.imprimir_red()

if __name__ == '__main__':
	main()
