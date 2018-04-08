 
class Listinfo(object):
	def __init__(self,*m):
		self.__list=list(m)
	def add_key(self,keyname):
		self.__list.append(keyname)
	def get_key(self,num):
		if isinstance(num,int):
		
			self.__num=num
			print("{}符合列表元素的条件！".format(num))
		else:
			raise ValueError("此元素无效！！")
	def update_list(self,l):
		if isinstance(l,list):
			self.__list=self.__list+l
		else:
			raise TypeError("该类型不匹配！！")

	def del_key(self,k):
		if len(self.__list)==0:
			raise EOFError("当前列表为空！！")
		elif len(self.__list)!=1:
			for i in self.__list:
				if i==k:
					self.__list.remove(k)
					return self.__list[-1]
			else:
				raise KeyError("该表中没有此元素！！")
		elif len(self.__list)==1:
			for i in self.__list:
				if i==k:
					self.__list.remove(k)
				else:
					raise KeyError("该表中没有此元素！！")
			raise EOFError("列表为空")
	def show_list(self):
		print(self.__list)
lis=Listinfo(5,6)
lis.add_key(4)
try:
	lis.get_key(4)
except ValueError as e:
	print("exception:%s"%e)
lis.update_list([2,3])
try:
	lis.show_list()
except TypeError as e:
	print("exception:%s"%e)

lis.del_key(6)
try:
	lis.show_list()
except (KeyError,EOFError):
	print("sorry")











