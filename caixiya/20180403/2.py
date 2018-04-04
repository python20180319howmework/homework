'''
2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''
class Bjhuanlegu(object):
	def __init__(self,price=100):
		self.__price=price
	def qnprice(self):
		return self.__price
	def stuprice(self):
		self.__price=self.__price/2
		return self.__price
	def vacation(self):
		self.__price=self.__price*1.2
		return self.__price

qn1=Bjhuanlegu()
qn2=Bjhuanlegu()
stu=Bjhuanlegu()
pr=qn1.qnprice()+qn2.qnprice()+stu.stuprice()
vac=qn1.vacation()+qn2.vacation()+stu.vacation()
print("两个社会青年和一个学生平日比节假日门票能省{}".format(vac-pr))
