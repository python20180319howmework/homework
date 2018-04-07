
#请利用@property为一个Screen类实例加上width和height以及获取和设置属性，在定义一个可以获取分辨率的方法

class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError("分辨率必须是整型数")
		if value < 0 :
			raise ValueError("分辨率必须是大于0的数")   
		self._width = value

	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError("分辨率必须是整型数")
		if value < 0 :
			raise ValueError("分辨率必须是大于0的数")   
		self._height = value
	
	@property
	def fenbianlv(self):
		return str(self._width)+"*"+str(self._height)

s = Screen()
s.width = 1920
s.height = 1080
print("分辨率为：{}".format(s.fenbianlv))


