"""
1.根据以下描述,尝试用程序呈现
   属性:长和宽
   方法:1)设置长和宽 2)获取长和宽 3)获取面积 
"""

class Co(object):
	
	def __init__(self,longth,wide):
		self.longth = longth #实例属性
		self.wide = wide
		#self.area = area
	def getCo(self):
		return (self.longth,self.wide) 	
	
	def setCo(self,newlong,newwide):
		self.length = newlong
		self.wide = newwide
	
	def getArea(self):
		#print("长是：{} 宽是：{} 面积是：{}".format(self.longth, self.wide, self.area))
		return self.longth*self.wide	
	
c = Co(10,5)  
"""
setattr(c, "longth", 11)
setattr(c, "wide",12 )
setattr(c,"area",11*12) 
c.getinfo()
""" 
#print(getattr(c,"longth"), getattr(c,"wide"),getattr(c,"area"))

print(c.getCo())
print(c.getArea())

c.setCo(11,2)
print(c.getCo())
print(c.getArea())

