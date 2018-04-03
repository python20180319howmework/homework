'''
根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''
class Test():
	def __init__(self,chang,kuan):
		self.__chang=chang
		self.__kuan=kuan
	def myck(self):
		print("长：{},宽：{}".format(self.__chang,self.__kuan))
	def myarea(self):
		print("面积为{}".format(self.__chang * self.__kuan))
	def setck(self,newchang,newkuan):
		self.__chang=newchang
		self.__kuan=newkuan
x,y=eval(input("please:"))
t=Test(x,y)
t.myck()
t.myarea()
t2=Test(8,9)
t2.myck()
t2.myarea()
t2.setck(8,5)
t2.myck()
t2.myarea()
		
		
