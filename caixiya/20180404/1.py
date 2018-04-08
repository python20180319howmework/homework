'''
property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法
'''
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,width):
		self._width= width
	
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,height):
		self._height=height
	@property
	def fbl(self):
		return self._width*self._height
s=Screen()
s.width=1024
s.height=1024
print(s.fbl)

