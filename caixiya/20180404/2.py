'''
2. 定义一个直线类(Line)和点类(Point),提供一个方法getLength方法,获取直线的长度
'''
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
		self._length = math.sqrt(pow(self._x,2) + pow(self._y,2))

	def getLength(self):
		return self._length

a = Point(-1,-1)
b = Point(1,1)
l = Line(a,b)

print("直线的长度为{:.2f}".format(l.getLength()))


