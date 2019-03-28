from selenium import webdriver
import time

class cambio_chingon():
	def __init__(self,pnum):
		self.pnum=pnum

	def swicheo(self):
		proxys=[{"http1":"187.188.213.4","Port1":56829},
				{"http2":"201.164.154.102","Port2":33478},
				{"http3":"189.203.179.18","Port3":8080},
				{"http4":"189.206.216.18","Port4":4145},
				{"http5":"38.123.64.233","Port5":31596},
				{"http6":"187.178.238.177","Port6":3629},
				{"http7":"189.201.241.69","Port7":4145},
				{"http8":"177.238.248.104","Port8":50916},
				{"http9":"38.124.200.65","Port9":31596},
				{"http10":"170.81.140.79","Port10":	61437},
				{"http11":"45.76.76.48","Port11":1080}]

		self.profile=webdriver.FirefoxProfile()
		self.profile.set_preference('network.proxy_type',1)
		self.profile.set_preference('network.proxy.http',proxys[self.pnum-1]["http"+str(self.pnum)])
		self.profile.set_preference('network.proxy.http_port',proxys[self.pnum-1]["Port"+str(self.pnum)])
		self.profile.update_preferences()
		return self.profile

	def pruebita(self):
		driver=webdriver.Firefox(firefox_profile=self.profile)
		driver.get('http://www.google.com')
		time.sleep(3)
		driver.close()

if __name__ == '__main__':
	a=cambio_chingon(11)
	a.swicheo()
	a.pruebita()