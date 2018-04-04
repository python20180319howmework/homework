


#1.根据以下描述,尝试用程序呈现
#   属性:长和宽
#   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
class Cft(object):
	def __init__(self , l,w):
		self.__l = l
		self.__w = w
	def setl(self,newl):
		self.__l = newl
	def setw(self,neww):
		self.__w = neww
	def pri_cft(self):
		print("长方体的长是{},长方体的宽是{}".format(self.__l,self.__w))

	def s(self):
		self.__s =self.__l * self.__w
		print("长方体的面积是{}".format(self.__s))
z1 = Cft(5,6)
z1.pri_cft()
z1.s()
z1.setl(9)
z1.setw(4)
z1.pri_cft()
z1.s()



