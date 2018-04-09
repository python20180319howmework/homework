class Listinfo(object):
	def __init__(self,*l):
		self.__list = list(l)
	def add_key(self,keyname):
		return self.__list.append(keyname)
	def get_key(self,num):
		if not isinstance(num,int):
			raise TypeError("this type is error")
		else:
			if num < 0 or num > len(self.__list) - 1:
				raise IndexError("this index is error")
			else:
				return self.__list[num]
	def update_list(self,l1):
		if isinstance(l1,list):
			self.__list = self.__list + l1
			return self.__list
		else:
			raise TypeError("this type is error")
	def del_key(self):
		if self.__list:
			self.__list.pop()
			return self.__list[-1]	
		else:
			raise EOFError("this list is over")
	def print_list(self):
		for i in self.__list:
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
