'''
根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''

class Rectangular(object):
	def  __init__(self,leng,wide):
		self.__leng = leng
		self.__wide = wide
	def setleng(self,newleng):     
		self.__leng = newleng
	def setwide(self,new_wide):
		self.__wide = new_wide
	def getleng(self):
		print("长为:{}".format(self.__leng))
	def getwide(self):
		print("宽为:{}".format(self.__wide))
	def s(self):
		print("面积为:{}".format(self.__leng*self.__wide))


c = Rectangular(5,6)

#设置长和宽
c.setleng(3)   
c.setwide(2)

#获取长和宽
c.getleng()
c.getwide()

#获取面积 
c.s()
