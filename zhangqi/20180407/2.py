#2. 定义一个直线类(Line)和点类(Point),提供一个方法getLength方法,获取直线的长度

from math import sqrt
#定义长度的算法
class Line(object):
	def __init__(self, a1, a2):
		self._x = a1.get_x() - a2.get_x()
		self._y = a1.get_y() - a2.get_y()
		self._length = sqrt(self._x ** 2 + self._y ** 2)

	def getLength(self):
		return self._length

# 获取两个点
class Point(Line):
	def __init__(self, x, y):
		self._x = x
		self._y = y
	def get_x(self):
		return self._x
	def get_y(self):
		return self._y


a1 = Point(0,0)
a2 = Point(0,2)
l = Line(a1,a2)
print("两点之间的直线长度为{}".format(l.getLength()))

