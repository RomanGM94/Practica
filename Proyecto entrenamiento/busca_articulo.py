from cadenota_cadenita import cadeniota
from perceptron_word import perceptron_mio

class buscador():
	def __init__(self,cadena,articulo):
		self.cadena=cadena
		self.articulo=articulo
	def busca(self):
		a=cadeniota(self.cadena)
		a.cadenita()
		#print(len(a.wwspace))
		#print(a.wwspace[0])
		numde=[]
		for i in range(len(a.wwspace)):
			de=perceptron_mio(a.wwspace[i],"de")
			de.identificador()
			numde.append(de.encontro)
		numpara=[]
		for i in range(len(a.wwspace)):
			para=perceptron_mio(a.wwspace[i],"para")
			para.identificador()
			numpara.append(para.encontro)
		print(numde)
		print(numpara)

		numarticulo=[]
		for i in range(len(a.wwspace)):
			b=perceptron_mio(a.wwspace[i],self.articulo)
			b.identificador()
			numarticulo.append(b.encontro)
		print(numarticulo)

		for i in range(len(numarticulo)):
			print(numarticulo[i])
			if numarticulo[i]==0:
				if i!=0:
					if numde[i-1]==0 or numpara[i-1]==0:
						self.hay=1
					else:
						self.hay=0
				else:
					self.hay=0
		if hasattr(self, 'hay'):
			print("")
		else:
			self.hay=1

		if self.hay==0:
			self.c="La cadena si contiene el articulo"
		else:
			self.c="La cadena NO contiene el articulo"

		return self.c,self.hay

if __name__ == '__main__':
	cadena="zapatos de son nuevos"
	articulo="zapatos"
	a=buscador(cadena,articulo)
	a.busca()
	print(a.c)
	print(a.hay)