'''
1,根据以下描述，尝试用程序实现
	属性：长和宽
	方法：1）设置长和宽  2）获取长和宽  3）获取面积

'''

class Box(object) :
	def __init__(self, chang,kuan):
		self.__chang = chang
		self.__kuan = kuan

	def setchang(self, newchang):	
		self.__chang = newchang

	def setkuan(self, newkuan):
		self.__kuan = newkuan

	def getck(self):
		print("长是：{}    宽是：{}".format(self.__chang,self.__kuan))

	def mianji(self):
		print("面积是{}".format(self.__chang*self.__kuan))


s = Box(1,1)

#设置长、宽
s.setchang(5)
s.setkuan(6)

#获取长、宽
s.getck()

#获取面积
s.mianji()


