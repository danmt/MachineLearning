from dependencias import *

def init():
	f, subplots = plt.subplots(2, sharex=True)

	#DATOS DE VALIDACION
	entrada = np.arange(-4, 4, 0.05)
	#DATOS DEL PROBLEMA
	datos = leer_datos('./pruebas/lab5/ejercicio1/datos/T5E1.xlsx')

	#
	#	ESTRATEGIA PARA ESCOGER CENTROS: SOM
	#

	som_plot = subplots[0]
	graficar_RBF('SOM',entrada,datos,som_plot)

	#
	#	ESTRATEGIA PARA ESCOGER CENTROS: Manual
	#

	cluster_plot = subplots[1]
	graficar_RBF('manualmente',entrada,datos,cluster_plot)

	plt.show()