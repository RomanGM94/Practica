from selenium import webdriver
from bs4 import BeautifulSoup
from limpieza_elementos import quita_elementos

class extraccion():
	def __init__(self,articulo):
		self.articulo=articulo

	def extraccion2(self):
		driver=webdriver.Firefox()

		contador1=1
		contadorauxiliar1=1
		contador2=contador1
		titulo_art={}
		precio_art={}
		descripcion_art={}
		imagenes_art={}
		ranking_art={}

		links_art={}
		link_aux={}

		url="https://listado.mercadolibre.com.mx/" + self.articulo + "#D[A:" + self.articulo + "]"
		driver.get(url)
		html=driver.page_source
		soup=BeautifulSoup(html,features="lxml")

		#Titulo del articulo
		'''for h in soup.find_all("span", class_="main-title"):
			x=h.text
			titulo_art.update({"Titulo_"+str(contador1):x})
			contador1=contador1+1
		contador1=contador2
		print(titulo_art)'''

		#Precio del articulo
		'''for h in soup.find_all("span", class_="price__fraction"):
			x=h.text
			precio_art.update({"Precio articulo_"+str(contador1):"$"+x})
			contador1=contador1+1
		contador1=contador2
		print(precio_art)'''

		#links del articulo
		for h in soup.find_all("a", href=True, class_="item__info-link item__js-link"):
			x=h['href']
			links_art.update({"link_art_"+str(contador1):x})
			contador1=contador1+1
		contador1=contador2
		
		print(links_art,"eso fue todo")
		
		#for c in range(len(links_art)):
		for c in range(3):
			url2=links_art["link_art_"+str(contador1)]
			driver.get(url2)
			html2=driver.page_source
			soup2=BeautifulSoup(html2,features="lxml")
			
			#Descripcion
			'''for h in soup2.select('div[class="item-description__text"]'):
				link_aux.update({"link_aux_"+str(contador1):h.text.replace("\n"," ")})'''
			
			#Imagenes
			for h in soup2.find_all("div", class_="gallery-content item-gallery__wrapper"):
				print(h["data-full-images"])
				imagenes_art.update({"imagenes_"+str(contador1):h["data-full-images"]})


			'''fotos_articulo=soup2.select('div[class="gallery-content item-gallery__wrapper"]')
			ft_a={}
			achiqiuta=fotos_articulo[0].attrs["data-full-images"]
			#["data-full-images"]
			print("fotos ",achiqiuta)
			print(type(achiqiuta))'''
			'''for c2 in range(len(fotos_articulo)):
				ft_p.update({"foto_"+str(contadorauxiliar1):fotos_propiedad[c2].attrs['href']})
				contadorauxiliar1=contadorauxiliar1+1
			contadorauxiliar1=1
			im_prop.update({"Fotos_"+str(contador1):ft_p})
			contador1=contador1+1'''

			'''for h in soup2.select('div[class="big-score"]'):
			#for h in soup2.find_all("a",clas_="iframe-modal"):
				#link_aux.update({"link_aux_":h["data-modal:url"]})
				print("link ",h)'''

			'''url3="https://articulo.mercadolibre.com.mx"+link_aux["link_aux_"]
			driver.get(url3)
			html3=driver.page_source
			soup3=BeautifulSoup(html3,features="lxml")'''





			#nombre de la propiedad
			#imagen_articulo=soup2.find(class_="col-md-10 header text-uppercase family-barlowSemiCondensedMedium").get_text()
			#name_prop.update({"Nombre de la propiedad_"+str(contador1):nombre_propiedad})
		
			#imagenes de la propiedad
			#fotos_propiedad=soup2.select('a[data-gallery=""]')
			#ft_p={}
			#for c2 in range(len(fotos_propiedad)):
				#ft_p.update({"foto_"+str(contadorauxiliar1):fotos_propiedad[c2].attrs['href']})
				#contadorauxiliar1=contadorauxiliar1+1
			#contadorauxiliar1=1
			#im_prop.update({"Fotos_"+str(contador1):ft_p})
			contador1=contador1+1
		print(imagenes_art)
		#contador1=len(link_dir)
		#contador2=contador1



		driver.close()
		

if __name__ == "__main__":
	word="zapatos"
	a=extraccion(word)
	a.extraccion2()
