

#2. 定义一个直线类(Line)和点类(Point),提供一个方法getLength方法,获取直线的长度

import math
class Len(object):
	@property	
	def line(self,length):
		return self._length 
		
class Point(object):


	ipt = input('请输入x1,y1,x2,y2，以逗号隔开:')
	data = ipt.split(',')
	data = [int(x) for x in data]
	result = math.sqrt(math.pow(data[0]-data[2],2)+math.pow(data[1]-data[3],2))
	print(data[0],',',data[1],'与',data[2],',',data[3],'之间的距离为：',result)


s1 =Point()





