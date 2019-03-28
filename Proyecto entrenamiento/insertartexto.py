import pymongo
from pprint import pprint

class escribe():
	def __init__(self,titulo,precio,descripcion,imagenes,ranking,producto):
		self.titulo=titulo
		self.precio=precio
		self.descripcion=descripcion
		self.imagenes=imagenes		
		self.ranking=ranking
		self.producto=producto

	def escribedoc(self):
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["proyecto_ent"]
		mycol = mydb[self.producto]
		x=mycol.insert_one({"Titulo":self.titulo,"Precio":self.precio,"Descripcción":self.descripcion,"Imagenes":self.imagenes,"Ranking":self.ranking})
		
	def findea(self):
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["proyecto_ent"]
		mycol = mydb[self.producto]
		y=mycol.find({"Titulo":self.titulo})
		for z in y:
			pprint(z)

	def findea_all(self):
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["proyecto_ent"]
		mycol = mydb[self.producto]
		y=mycol.find({})
		for z in y:
			pprint(z)

if __name__ == '__main__':
	titulo="Carro Ultimo Modelo"
	precio="$3000000"
	descripcion="Carrito azul"
	imagenes="Esta deberia ser una imagen"
	ranking="4 estrellas"
	producto="Carro"
	a=escribe(titulo,precio,descripcion,imagenes,ranking,producto)
	a.escribedoc()
	a.findea()
	a.findea_all()