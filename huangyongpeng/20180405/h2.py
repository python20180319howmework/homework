
'''
定义一个直线类(Line)和点类(Point),提供一个方法getLength方法,获取直线的长度
'''
import math
class Point(object):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def showX(self):
		return self.__x
	def showY(self):
		return self.__y
		
class Line():
	def __init__(self,m,n):
		self.__x=n.showX()-m.showX()
		self.__y=n.showY()-m.showY()
	
		
	def getLength(self):
	
		return math.sqrt(self.__x*self.__x+self.__y*self.__y)
	

p1=Point(2,3)
p2=Point(5,7)
l=Line(p1,p2)
print("俩点的距离是：{}".format(l.getLength()))

