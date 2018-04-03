#1.根据以下描述,尝试用程序呈现
#   属性:长和宽
#   方法:1)设置长和宽 2)获取长和宽 3)获取面积 

class Cfx(object):
	def __init__(self,length1,width1):
		self.__length1 = length1
		self.__width1 = width1
	def pri_cfx(self):
		print("长方形的长和宽分别为{}，{}".format(self.__length1,self.__width1))
	def setlength1(self,newlength1):
		self.__length1 = newlength1
	def setwidth1(self,newwidth1):
		self.__width1 = newwidth1
	def cj(self):
		self.__cj = self.__length1 * self.__width1
		print("长方形的面积为{}".format(self.__cj))

if __name__ == "__main__":
	l = Cfx(2,5)
	l.pri_cfx()
	l.cj()
	l.setlength1(5)
	l.setwidth1(10)		
	l.pri_cfx()
	l.cj()













