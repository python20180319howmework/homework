'''
2.定义一个北京欢乐谷门票类,应用你所定义的类,计算两个社会青年和一个学生平日比节假日门票能省多少钱
    票价是:
        除节假日票价100元/天
        节假日为平日的1.2倍
        学生半价
'''
class Menpiao(object):
	def run(self):
		pass
class Qingnian(Menpiao):
	def run(self):
		s = (100 * 1.2 - 100) * 2
		print("两个青年平日比节假日门票能省{}元钱".format(s))
class Xuesheng(Menpiao):
	def run(self):
		x = (100 * 1.2 - 100) / 2
		print("一个学生平日比节假日能省{}元钱".format(x))
def show(pri):
	pri.Menpiao()

qing = Qingnian()
qing.run()
xue = Xuesheng()
xue.run() 			

































