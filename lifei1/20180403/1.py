'''
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''
class Suqare(object):
	def __init__(self,long1,wide):
		self.long1=long1
		self.wide =wide
	def setlw(self,newlong1,newwide):
		self.long1=newlong1
		self.wide =newwide
	def mianji(self):
		print("面积为:{}".format(self.long1*self.wide))
c=Suqare(5,6)
c.mianji()
c.setlw(6,7)
c.mianji()
c1=Suqare(1,2)
print("宽为：",getattr(c1,"wide"))
print("长为：",getattr(c1,"long1"))
