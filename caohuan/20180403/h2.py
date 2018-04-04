'''
2,定义一个北京欢乐谷门票类，应用你所定义的类，计算两个社会青年和一个学生平日比节假日门票能省多少钱
	票价是：
		除节假日票价100元/天
		节假日为平日的1.2倍
		学生半价
'''
class Ticket(object):
	def __init__(self,adultprice,stuprice):
		self.__adultprice = adultprice
		self.__stuprice = stuprice
	def pri_1(self):
		print("平日成人票价为{}元,学生票价为{}元。".format(self.__adultprice,self.__stuprice))
	def pri_2(self):
		print("假日成人票价为{}元,学生票价为{}元。".format(self.__adultprice * 1.2,self.__stuprice * 1.2))
	def panduan(self,a,b):
		x = self.__adultprice*a+self.__stuprice*b
		y = (self.__adultprice*a+self.__stuprice*b)*1.2
		print("{}个成人{}个学生平日里要{}元。节假日要{}元。能省{}元".format(a,b,x,y,y - x))
s = Ticket(100,50)
s.pri_1()
s.pri_2()         

s.panduan(2,1) 





