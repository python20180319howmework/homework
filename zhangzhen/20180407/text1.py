#1.请利用@property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法
#1.定义一个Screen 类
class Screen(object):
	@property
	def myScreen(self,length,width):
		return self.__length 
		return self.__width
	@myScreen.setter
	def myScreen(self,length):
		self.__length ,self.__width = length
	@property
	def newScreen(self):
		return (self.__length *self.__width)

s1 = Screen()
s1.myScreen = 10,20
print(s1.newScreen)


































