from guarda_documento import salvador
from insertartexto import escribe
from random import randint

class documentos_100():
	def __init__(self,n,titulo,precio,descripcion,imagenes,ranking,producto):
		self.n=n
		self.titulo=titulo
		self.precio=precio
		self.descripcion=descripcion
		self.imagenes=imagenes		
		self.ranking=ranking
		self.producto=producto

	def n_documentos(self):
		for i in range(self.n):
			a=salvador(self.titulo['titulo'+str(i)],self.precio['precio'+str(i)],self.descripcion['descripcion'+str(i)],self.imagenes['imagenes'+str(i)],self.ranking['ranking'+str(i)],self.producto)
			a.savage()
		b=escribe(self.titulo,self.precio,self.descripcion,self.imagenes,self.ranking,self.producto)
		b.findea_all()

if __name__ == '__main__':
	n=100
	titulo={}
	precio={}
	descripcion={}
	imagenes={}
	ranking={}

	for i in range(n):
		titulo.update({"titulo"+str(i):"para Zapatos Ultimo Modelo"})
		precio.update({"precio"+str(i):randint(500,50000)})
		descripcion.update({"descripcion"+str(i):"Zapatito azul"})
		imagenes.update({"imagenes"+str(i):"Esta deberia ser una imagen"})
		ranking.update({"ranking"+str(i):str(randint(1,5))+" estrellas"})
	
	producto="Zapato"


	a=documentos_100(n,titulo,precio,descripcion,imagenes,ranking,producto)
	a.n_documentos()