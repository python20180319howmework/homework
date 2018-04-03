'''
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
'''
class Changfangxing(object):
	count = 0
	def __init__(self, chang, kuan):
		self.chang = chang
		self.kuan = kuan
	def getCount(self):
		return self.count

x = Changfangxing(20, 10)
c = getattr(x,"chang")
k = getattr(x,"kuan")
print(getattr(x,"chang"))
print(getattr(x,"kuan"))
s = c * k
print(s)


































