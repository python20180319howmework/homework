"""
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
"""

class Co(object):
	
	def __init__(self,longth,wide,area):
		self.longth = longth #实例属性
		self.wide = wide
		self.area = area	
		
	def getinfo(self):
		print("长是：{} 宽是：{} 面积是：{}".format(self.longth, self.wide, self.area))

	
c = Co("longth","wide","area")  

setattr(c, "longth", 11)
setattr(c, "wide",12 )
setattr(c,"area",11*12) 
c.getinfo() 
#print(getattr(c,"longth"), getattr(c,"wide"),getattr(c,"area"))




