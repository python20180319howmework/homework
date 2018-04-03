'''
定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''

class Tickets(object):
	def __init__(self,*,price = 100):
		self.__price = price
	def vacation(self):
		self.__price = self.__price * 1.2
		return self.__price
	def student(self):
		self.__price = self.__price * 0.5
		return self.__price
	def myprint(self):
		return self.__price

a = Tickets()
b = Tickets()
c = Tickets()

s1 = a.myprint() + b.myprint() + c.student()

s2 = a.vacation() + b.vacation() + c.vacation()

s = s2 - s1
print("两个社会青年和一个学生平日比节假门票能省{}元".format(s))
