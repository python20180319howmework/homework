
#定义一个直线类(Line)和点类(Point)，提供一个方法getLength方法，获取直线的长度
import math 

class Point(object):
	def __init__(self,x,y):
		self._x = x
		self._y = y

	def getx(self):
		return self._x

	def gety(self):
		return self._y

class Line(Point):
	def __init__(self,a,b):
		self._x = a.getx() - b.getx()
		self._y = a.gety() - b.gety()
		self._len = math.sqrt(self._x ** 2 + self._y ** 2)

	def getLength(self):
		return self._len

a = Point(0,0)
b = Point(1,1)
l = Line(a,b)

print("直线长度为:{}".format(l.getLength()))




