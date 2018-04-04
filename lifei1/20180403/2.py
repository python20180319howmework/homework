'''
2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''


class Price(object):
	price=0
	price1=0
	def __init__(self,student,shehui):
		self.__student=student
		self.__shehui =shehui
	def pingri(self):
		price=100*1.2*self.__shehui+100*1.2*self.__student//2
		price1=100*self.__shehui+100*self.__student//2
		print("能省",price-price1)
c=Price(1,2)
c.pingri()
		
