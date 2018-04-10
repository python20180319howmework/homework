'''
2. 定义一个列表操作类:Listinfo
   1) 方法:
      1- 列表元素的添加 (添加的元素必须是字符串或者整型数)
      2- 取值
      3- 合并
      4- 删除并返回最后一个元素  
'''
class Listinfo(object):
	def __init__(self, ls):
		self.__ls = ls
		
	def addElm(self, elm):
		if isinstance(elm, (int, str)) == False:
			raise ValueError("你所插入列表的元素类型不符合整型或者字符串要求")
		self.__ls.append(elm)
	
	def fetchElm(self, ind):
		if ind < 0 or ind >= len(self.__ls):
			raise IndexError("你所传递的索引值超出了列表的范围")
		return self.__ls[ind]
	
	def combList(self, newlist):
		self.__ls.extend(newlist)

	def delList(self):
		if len(self.__ls) == 0:
			raise StopIteration("你要删除的列表是一个空列表")
		return self.__ls.pop(-1)
	
	def showList(self):
		for i in self.__ls:
			print(i, end=" ") 
		print("")

l = Listinfo([1,2])
l.addElm(1)
l.addElm("hello")
l.showList()
print("列表索引2对应的值为{}".format(l.fetchElm(2)))
l.combList(["a", 'b', 11, 22])
l.showList()
print("最后一个元素是：{}".format(l.delList()))
l.showList()
