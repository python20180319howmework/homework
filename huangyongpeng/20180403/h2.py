
'''
定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''
class Menpiao(object):
	def __init__(self,items):
		self.__qnrenshu=items[0]
		self.__xsrenshu=items[1]
	def duoyu(self):
		k=(self.__qnrenshu)*100*0.2+(self.__xsrenshu)*100*0.2*0.5
		print("{}名青年和{}名学生平日比节假日省{}元".format(self.__qnrenshu,self.__xsrenshu,k))
		
g=Menpiao(eval(input("请输入青年人数和学生人数：")))
g.duoyu()	









