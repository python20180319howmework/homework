#2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
#    票价是:
#        除节假日票价100元/天
#        节假日为平日的1.2倍
#        学生半价


class Per_piao(object):
	def __init__(self,usual,jjr):
		self.__usual = usual
		self.__jjr = jjr
	def pri_pi(self):
		print("北京欢乐谷平时门票价钱为{},节假日票价为{}".format(self.__usual,self.__jjr))
	def sum1(self):
		self.__sum1 = self.__jjr - self.__usual
		print("一个社会青年平时比节假日去欢乐谷省{}".format(self.__sum1))
		return self.__sum1
class Stu_piao(Per_piao):
	def __init__(self, usual, jjr):
		self.__usual = usual//2
		self.__jjr = jjr//2
	def pri_si(self):
		print("北京欢乐谷学生平时票价为{},节假日票价为{}".format(self.__usual,self.__jjr))
	def sum2(self):
		self.__sum2 = self.__jjr - self.__usual
		print("一个学生平时比节假日去欢乐谷省{}".format(self.__sum2))
		return self.__sum2
person1 = Per_piao(100, 120)
person1.sum1()
student = Stu_piao(100, 120)
student.sum2()

sum3= 0
sum3 = person1.sum1()*2 + student.sum2()
print(sum3)

















