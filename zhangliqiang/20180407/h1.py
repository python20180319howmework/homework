#1.请利用@property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法

class Screen(object):
	@property
	def fenbianlv(self,width,height):
		return self._width
		return self._height
	@fenbianlv.setter
	def fenbianlv(self,width):
		(self._width,self._height) = width
		

	@property
	def fenb(self):
		return self._width*self._height
s1 = Screen()
s1.fenbianlv = 1920,1048
print(s1.fenb)





#3题先枚举
