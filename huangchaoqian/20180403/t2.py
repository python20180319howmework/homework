'''
定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''
class Ticket():
	def __init__(self,price=100):
		self.__price=price
	def teenager(self):
		return self.__price
#		print("社会青年的票价为：{}".format(self.__price))
	def student(self):
		return self.__price/2
#		print("学生的票价为：{}".format(self.__price/2))
	def setprice(self):
#  		newprice=self.__price*1.2
#		self.__price=newprice
		self.__price*=1.2
def savemoney(m1,m2):
		return m2-m1

t=Ticket()
t1=t.teenager()
t.setprice()
t2=t.teenager()

save1=savemoney(t1,t2)

stu=Ticket()
st1=stu.student()
stu.setprice()
st2=stu.student()

save2=savemoney(st1,st2)
x,y=eval(input("please input teenagernum x and studentnum y:"))
print("{}个社会青年和{}个学生平日比节假日门票能省{}元".format(x,y,x*save1+save2*y))

