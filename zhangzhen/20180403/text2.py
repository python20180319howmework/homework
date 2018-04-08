
'''
2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''
class Tickets(object):
	def __init__(self,personp,studentp):
		self.__personp = personp
		self.__studentp = studentp
	def anualt(self):
		print("除节假日外，成人票价{} 学生票价{}".format(self.__personp,self.__studentp ))
	def fastablet(self):
		print("节假日，成人票价{} 学生票价{}".format(self.__personp *1.2,self.__studentp *  1.2))
	def priced(self,x,y):
		mysum = 0.2 * (x * self.__personp + y * self.__studentp )
		print("平日比节假日少花{}元".format(mysum))
t = Tickets(100,50)

t.anualt()
t.fastablet()
t.priced(2,1)













