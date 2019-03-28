class quita_elementos():
	def __init__(self,cadenota):
		self.cadenota=cadenota
	def cadenita(self):
		self.wwelementos=[]
		cade=""
		for i in self.cadenota:
			if i=="<":
				self.wwelementos.append(cade)
				cade=""
			elif i==">":
				cade=""
			else:
				cade=cade+i
		#print(self.wwspace)
		return self.wwelementos

if __name__ == '__main__':
	#cadenota=input("Introduce una cadena de caracteres: ")
	cadenota="<span class=main-title> Zapato Derby Flexi Caballero 58301 Negro </span>"
	a=quita_elementos(cadenota)
	a.cadenita()
	print(a.wwelementos[1])