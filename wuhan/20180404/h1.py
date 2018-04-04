'''
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''

class Rectangle(object):
	def __init__(self,longth,width):
		self.__longth = longth
		self.__width = width
	def wuhan(self):
		print("矩形的长为{},宽为{},面积为{}".format(self.__longth,self.__width,self.__longth * self.__width))

jx = Rectangle(9,5)
jx.wuhan()
		
