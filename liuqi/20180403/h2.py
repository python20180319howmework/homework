"""
2.定义一个北京欢乐谷门票类,应用你所定义的类,
  计算两个社会青年和一个学生平日比节假日门票能省多少钱
  票价是:
  除节假日票价100元/天
  节假日为平日的1.2倍
  学生半价
"""

class Ticket(object):
	
	def __init__(self,species):
			self.__species = species
	def myprice(self):
		if self.__species == True:
			vacationprice = 1.2*100*0.5 
			usualprice = 100*0.5
			sprice = vacationprice - usualprice
			return sprice
		
		if self.__species == False:
			vacationprice = 1.2*100*2
			usualprice = 100*2
			mprice = (vacationprice - usualprice)
			return mprice


societyman = False
student = True

m = Ticket(societyman)
m1 = m.myprice()

s = Ticket(student)
s1 = s.myprice()

print("欢乐谷一个学生平日比节假日门票能节省{}元".format(s1))
print("欢乐谷一个社会青年平日比节假日门票能节省{}元".format(m1))
