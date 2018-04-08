#1.请利用@property为一个Screen类实例加上width和height的获取和设置属性,在定义一个可以获取分辨率的方法

class Screen(object):
	@property
	def fbl(self):
		return self._width, self._height
	@fbl.setter
	def fbl(self,screen):
		(self._width, self._height) = screen
	@property
	def get(self):
		return self._width, self._height


a = Screen()
a.fbl = 1600,800

print(a.fbl)
print("屏幕分辨率为{}".format (a.get))





