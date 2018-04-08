'''
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''
class Funn(object):
	mj=0
	def __init__(self,length,width):
		self.length=length
		self.width=width
		self.mj=self.length*self.width

	def getmj(self):
		return self.mj

f=Funn(20,10)
print(getattr(f,"length"))
print(getattr(f,"width"))
setattr(f,"length",40)
setattr(f,"width",30)
print(getattr(f,"length"))
print(getattr(f,"width"))
print(f.getmj())
