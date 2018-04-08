
'''
定义一个列表的操作类：
Listinfo
包括的方法：
1列表元素添加：add_key(keyname)[keyname:字符串或者整数类型]
2列表元素取值：get_key(num)[num:整数类型]
3列表合并：update_list(list)[list:列表类型]
4删除并且返回最后一个元素del_key()

'''
class Listinfo(object):
	def __init__(self,*l):
		self._list = list(l)

	def add_key(self,keyname):
		return self._list.append(keyname)

	def get_key(self,num):
		if not isinstance(num,int):
			raise TypeError("this type is error")
		else:
			if num < 0 or num > len(self._list) - 1:
				raise IndexError("this index is error")
			else:
				return self._list[num]

	def update_list(self,l1):
		if isinstance(l1,list):
			self._list = self._list + l1
			return self._list
		else:
			raise TypeError("this type is error")

	def del_key(self):
		if self._list:
			self._list.pop()
			return self._list[-1]	
		else:
			raise EOFError("this list is over")
	def print_list(self):
		for i in self._list:
			print(i,end = ',')
		print("")

s = Listinfo(1,2,3,4,5)
s.add_key(5)
s.print_list()
print(s.get_key(2))
a = Listinfo()
print(s.del_key())
b = [1,2,3,4]
c = 1
print(s.update_list(b))






