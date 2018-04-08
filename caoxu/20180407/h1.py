'''
请利用@property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法
'''

class Screen(object):
	@property
	def set_s(self):
		return self.__width,self.__height

	@set_s.setter
	def set_s(self,screen):
		(self.__width,self.__height) = screen
		
	@property
	def getscreen(self):
		return self.__width ,self.__height


s = Screen()
s.set_s = 800,600

print(s.set_s)
print("屏幕分辨率为{}".format(s.getscreen))

