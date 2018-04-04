


#2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
#    票价是:
#        除节假日票价100元/天
#        节假日为平日的1.2倍
#        学生半价


class Menpiao(object):
	def __init__(self,puprice,teprice):
		self.__puprice = puprice
		self.__teprice = teprice
	def pri_piao(self):
		print("北京欢乐谷平日票价为{},节日票价为{}".format(self.__puprice,self.__teprice))

		
	def getinfo(self):
		print("{}{}".format(self.__puprice,self.__teprice))
class Qingnian(Menpiao):
	def __init__(self,puprice,teprice):
		Menpiao.__init__(self,puprice,teprice)
	
class Student(Menpiao):
	def __init__(self,banpuprice,banteprice):
		Menpiao.__init__(self,banpuprice,banteprice)
		self.__banpuprice = banpuprice
		self.__banteprice = banteprice
	def getmyinfo(self):
		self.getinfo()
		print("学生票平日半价是{},学生票节假日半价是{}".format(self.__banpuprice,self.__banteprice))
	
	def sum1(self):
		self.__sum1	 = self.__teprice  - self.__puprice
		print("一个青年平日比节日门票省{}".format(self.__sum1))
		return self.__sum1
	def sum2(self):
		self.__sum2 = self.__banteprice -self.__banpuprice
		print("一个学生平日比节日门票省{}".format(self.__sum2))
		return self.__sum2
	def sum3(self):
		self.__sum3 = self.__sum1 * 2 + self.__sum2
		print("两个青年一个学生平日比节日一共省{}".format(self.__sum3))
		return self.__sum3

s1 = Menpiao(100,120)
s1.pri_piao()

q1 = Qingnian(100,120)
q1.pri_piao()

xs = Student(50,60)
xs.pri_piao()
xs.getmyinfo()

print(sum3())
