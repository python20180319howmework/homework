
class Mianji(object):
	def __init__(self,items):
		
		self.__chang=items[0]
		self.__kuan=items[1]
	
	def getck(self):
		print("长是：{} 宽是：{}".format(self.__chang,self.__kuan))
	def getmj(self):
		mj=int(self.__chang)*int(self.__kuan)
		print("面积是：{}".format(mj))
		
s=Mianji(eval(input("请输入长宽:")))
s.getck()
s.getmj()

