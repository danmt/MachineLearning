from Neurona import Neurona_oculta, Neurona_salida

class Capa_oculta:
	def __init__(self,dimensiones,funcion):
		self.neuronas = [None] * dimensiones
		self.dimensiones = dimensiones
		self.funcion = funcion

	def asignar(self,dim_entrada):
		for i in xrange(0,self.dimensiones):
			self.neuronas[i] = Neurona_oculta(self.funcion,dim_entrada)

	def asignar_anchuras(self,anchuras):
		for i, anchura in enumerate(anchuras):
			self.neuronas[i].asignar_anchura(anchura)

	def asignar_centros(self,centros):
		for i, centro in enumerate(centros):
			for j, coord in enumerate(centro):
				self.neuronas[i].asignar_centro(j,coord)

	def calcular(self,entrada):
		for i, neurona in enumerate(self.neuronas):
			neurona.calcular(entrada)
	
class Capa_salida:
	def __init__(self,dimensiones,funcion):
		self.neuronas = [None] * dimensiones
		self.dimensiones = dimensiones
		self.funcion = funcion

	def asignar(self,dim_entrada):
		for i in xrange(0,self.dimensiones):
			self.neuronas[i] = Neurona_salida(self.funcion,dim_entrada)

	def asignar_pesos(self,pesos):
		for i, peso in enumerate(pesos):
			for j, neurona in enumerate(self.neuronas):
				neurona.asignar_peso(i,peso[j])

	def asignar_sesgos(self,sesgos):
		for i, sesgo in enumerate(sesgos):
			self.neuronas[i].asignar_sesgo(sesgo)

	def calcular(self,capa_oculta):
		for i, neurona in enumerate(self.neuronas):
			neurona.calcular(capa_oculta)