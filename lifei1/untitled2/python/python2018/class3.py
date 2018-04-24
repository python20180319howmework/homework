class Printmanchine(object):
	def pri(self):
		print("能打印东西")

class Heibai(Printmanchine):
	def pri(self):
		print("黑白打印机打印黑白字")

class Caise(Printmanchine):
	def pri(self):
		print("彩色打印机能打印照片")

def show(p):
	p.pri()
	p.pri()

p1=Printmanchine()
show(p1)

heibai=Heibai()
show(heibai)

caise=Caise()
show(caise)
