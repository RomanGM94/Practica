class cadeniota():
	def __init__(self,cadenota):
		self.cadenota=cadenota
	def cadenita(self):
		self.wwspace=[]
		cade=""
		for i in self.cadenota:
			if i==" ":
				self.wwspace.append(cade)
				cade=""
			else:
				cade=cade+i
		self.wwspace.append(cade)
		#print(self.wwspace)
		return self.wwspace

if __name__ == '__main__':
	cadenota=input("Introduce una cadena de caracteres: ")
	print(cadenota.isspace())
	a=cadeniota(cadenota)
	a.cadenita()
	print(a.wwspace)
