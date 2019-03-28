from insertartexto import escribe
from busca_articulo import buscador

class salvador():
	def __init__(self,titulo,precio,descripcion,imagenes,ranking,producto):
		self.titulo=titulo
		self.precio=precio
		self.descripcion=descripcion
		self.imagenes=imagenes		
		self.ranking=ranking
		self.producto=producto

	def savage(self):
		a=buscador(self.titulo,self.producto)
		a.busca()
		print(a.c)
		if a.hay==0:
			b=escribe(self.titulo,self.precio,self.descripcion,self.imagenes,self.ranking,self.producto)
			b.escribedoc()

if __name__ == '__main__':
	titulo="Zapatos Ultimo Modelo"
	precio="$3000000"
	descripcion="Carrito azul"
	imagenes="Esta deberia ser una imagen"
	ranking="4 estrellas"
	producto="Zapato"
	a=salvador(titulo,precio,descripcion,imagenes,ranking,producto)
	a.savage()