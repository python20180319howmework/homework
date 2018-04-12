'''
定义一个列表的操作类Listinfo
1.列表元素添加 add_key(keyname) [keyname:字符串或者整数型]
2。列表元素取值 get_key(num) [num: 整数型]
3.列表合并 update_list(list)  [list,列表类型]
4.删除并返回最后一个元素
'''

class Listinfo(object):
	def __init__(self,l):
		self.__l = list(l)
	def add_key(self,keyname):
		if isinstance (keyname,(int,str)) == False:
			raise ValueError("you are wrong")
		self.__l.append(keyname)
	def get_key(self,num):
		if not isinstance(num,int):
			raise TypeError("the num is wrong")
		if num < 0 or num > len(self.__l) - 1:
			raise IndexError("the len is wrong")
		return self.__l[num]
	def update_list(self,l1):
		self.__l.extend(l1)
	def del_key(self):
		if len(self.__l) == 0:
			raise StopIteration("kong ")
		return self.__l.pop(-1)
	def show_list(self):
		for i in self.__l:
			print(i, end = "," )
		print("")

m = Listinfo([1,2,3,4,5,6,7,8,9])

m.add_key(0)
m.show_list()

n = m.get_key(5)
print(n)

o = m.del_key()
print(o)

p = [10,11,12]
q = m.update_list(p)
print(q)

























