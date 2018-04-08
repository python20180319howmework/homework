#2. 定义一个直线类(Line)和点类(Point),提供一个方法getLength方法,获取直线的长度

import math
class Point(object):

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

class Line(object):
    
    def __init__(self,p1,p2):
        self.__x = p1.getX() - p2.getX()
        self.__y = p1.getY() - p2.getY()
        self.__len = math.sqrt(self.__x*self.__x + self.__y*self.__y)
    def getLen(self):
        return self.__len		


p1 = Point(10,20)
p2 = Point(10,10)
m = Line(p1,p2)
n = m.getLen()
print(n)
































