def comb_lineal(x,w):
	suma = 0

	for i, xi in enumerate(x):
		suma = suma + (xi * w[i])

	return suma