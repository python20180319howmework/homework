
'''
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 


'''
	
class Area(object):
	def __init__(self,length,width):
		self.__length =length
		self.__width = width
	def getinfo(self):
		print("矩形的长是{} 矩形的宽是{}".format(self.__length,self.__width))
	def setlength(self,newlength):
		self.__length = newlength
	def setwidth(self,newwidth):
		self.__width = newwidth
	def myarea(self):
		print("矩形的面积是{}".format((self.__length*self.__width)))
	def getlength(self):
		print("矩形的长是{}".format(self.__length))
	def getwidth(self):
		print("矩形的宽是{}".format(self.__width))
s = Area(10,100)
s.getinfo()
s.myarea()

s.setlength(20)
s.setwidth(200)
s.getinfo()
s.myarea()

s.getlength()
s.getwidth()
s.myarea()





























