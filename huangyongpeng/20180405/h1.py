
'''
请利用@property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法
'''
class Screen(object):
	@property
	def chang(self):
		return self.__width
	@chang.setter
	def chang(self,width):
		self.__width=width
	@property
	def kuan(self):
		return self.__height
	@kuan.setter
	def kuan(self,height):
		self.__height=height
	@property
	def getfenbianlv(self):
		return str(self.__width)+"*"+str(self.__height)
		
s=Screen()
s.chang=1024
s.kuan=768
print(s.getfenbianlv)	


