from mlxtend.classifier import Perceptron
import os
import numpy as np

class perceptron_mio():
	def __init__(self,word,comparar):
		self.word=word.lower()
		self.comparar=comparar.lower()
		self.encontro=3

	def identificador(self):
		w_prueba=[]
		Elementos=[self.word,self.comparar]
		auxiliar_contador=0;
		for j in Elementos:
			if len(self.word)<=len(j):
				for i in range(len(self.word)):
					if self.word[i]==j[i]:
						w_prueba.append(1)
					else:
						w_prueba.append(0)
			else:
				for i in range(len(j)):
					if self.word[i]==j[i]:
						w_prueba.append(1)
					else:
						w_prueba.append(0)
		#print (w_prueba)
		#print(sum(w_prueba[:len(self.word)]))
		auxiliar_x=sum(w_prueba[:len(self.word)])
		#print(auxiliar_x)
		auxiliar_x2=sum(w_prueba[len(self.word):len(self.word)+len(self.comparar)])
		#print(auxiliar_x2)
		X=np.array([
			[len(self.word), sum(w_prueba[:len(self.word)])],
			[len(self.word), sum(w_prueba[:len(self.word)])],
			[len(self.word), sum(w_prueba[1:len(self.word)])],
			[len(self.word), sum(w_prueba[1:len(self.word)])],
			[len(self.word)+1, len(self.word)-1],
			[len(self.word)-1, len(self.word)-1],
			[len(self.word)+1, len(self.word)-2],
			[len(self.word)-1, len(self.word)-2]
			])
		#print(X[:,0])
		X[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
		X[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()
		y=np.array([0,0,0,0,1,1,1,1])
		#print(X)
		#print(y)
		ppn = Perceptron(epochs=5, 
                 eta=0.05, 
                 random_seed=0,
                 print_progress=3)
		ppn.fit(X, y)
		X2=(np.array([
			[len(self.word), auxiliar_x],
			[len(self.word)+1, len(self.word)-1],
			[len(self.comparar),auxiliar_x2]
			]))
		#print("\n",X2[:,0].std())
		#print("\n",X2[:,1].std())
		X2[:,0] = (X2[:,0] - X2[:,0].mean()) / X2[:,0].std()
		X2[:,1] = (X2[:,1] - X2[:,1].mean()) / X2[:,1].std()
		#print(X2)
		#print("\n",ppn.predict(X2))
		resultado=ppn.predict(X2)
		self.encontro=resultado[2]
		print("\n\n")
		a=os.system("clear")
		return self.encontro

if __name__ == '__main__':
 	#word=input("Introduce la palabra a buscar: ")
 	word="Zapato"
 	#comparar=input("Introduce la palabra a comparar: ")
 	comparar="zapato"
 	p=perceptron_mio(word.lower(),comparar.lower())
 	p.identificador() 
 	print("la palabra: ",p.encontro)