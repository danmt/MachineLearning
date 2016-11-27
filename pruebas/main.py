import sys
import os
import time

from pruebas.lab5.ejercicio1.main import init as lab5ejercicio1
from pruebas.lab5.ejercicio2.main import init as lab5ejercicio2

laboratorios = [
	dict({
		'numero':5,
		'ejercicios':[{
			'numero': 1,
			'init': lab5ejercicio1 
		}, {
			'numero': 2,
			'init': lab5ejercicio2 
		}]
	})
]

def listar_laboratorios(laboratorios):
	print("Laboratorios:")

	for i, lab in enumerate(laboratorios):
		print(str(i + 1) + ") Laboratorio " + str(lab['numero']) + ".")

def listar_ejercicios(ejercicios):
	print("Ejercicios:")

	for i, ejer in enumerate(ejercicios):
		print(str(i + 1) + ") Ejercicio " + str(ejer['numero']) + ".")



def main():
	menu_laboratorios = True

	while menu_laboratorios:
		os.system('clear')
		
		listar_laboratorios(laboratorios)
		# print("Laboratorios:")

		# for i, lab in enumerate(laboratorios):
		# 	print(str(i + 1) + ") Laboratorio " + str(lab['numero']) + ".")

		try:
			opcion_lab = int(raw_input('Seleccion: '))

			if opcion_lab < 1 or opcion_lab > len(laboratorios):
				print("Esa opcion no existe.")
				time.sleep(2)
				continue
			else:
				laboratorio = laboratorios[opcion_lab - 1]
				ejercicios = laboratorio['ejercicios']

				listar_ejercicios(ejercicios)
				# print("Ejercicios:")

				# for i, ejer in enumerate(ejercicios):
				# 	print(str(i + 1) + ") Ejercicio " + str(ejer['numero']) + ".")

				menu_ejercicios = True

				while menu_ejercicios:
					try:
						opcion_ejer = int(raw_input('Seleccion: '))
					
						if opcion_ejer < 1 or opcion_ejer > len(ejercicios):
							print("Esa opcion no existe.")
							continue
						else:
							os.system('clear')
							ejercicio = ejercicios[opcion_ejer - 1]

							print("Ejecutandose el ejercicio " + str(ejercicio['numero'])),
							print("del laboratorio " + str(laboratorio['numero']))
							print("")

							ejercicio['init']()
							
							menu_continuar = True

							while menu_continuar:
								opcion_continuar = raw_input('Deseas continuar? (S/N) ')

								opcion_continuar = opcion_continuar.lower()

								if (opcion_continuar == 's'):
									menu_continuar = False
									menu_ejercicios = False
									os.system('clear')

								elif (opcion_continuar == 'n'):
									menu_continuar = False
									menu_ejercicios = False
									menu_laboratorios = False
									print("\nByee...")
								else:
									print("Esa opcion no existe.")
									continue

					except ValueError:
						print('La opcion debe ser un numero.')
						time.sleep(2)

		except ValueError:
			print('La opcion debe ser un numero.')
			time.sleep(2)