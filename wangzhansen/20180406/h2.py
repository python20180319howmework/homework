

import math 

class Point(object):
	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def getx(self):
		return self.__x

	def gety(self):
		return self.__y

class Line(object):
	def __init__(self,a1,a2):
		self.__x = a1.getx() - a2.getx()
		self.__y = a1.gety() - a2.gety()
		self.__len = math.sqrt(self.__x ** 2 + self.__y ** 2)

	def getLength(self):
		return self.__len

a1 = Point(1,2)
a2 = Point(4,18)
l = Line(a1,a2)

print("直线长度为:{}".format(l.getLength()))
