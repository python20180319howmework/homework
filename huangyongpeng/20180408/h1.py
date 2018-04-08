class Student(object):
	def __init__(self,name,age,china,math,english):
		self.__name=name
		self.__age=age
		self.__c=china
		self.__m=math
		self.__e=english
		if self.__c<0 or self.__c>100 or self.__m<0 or self.__m>100 or self.__e<0 or self.__e>100:
			raise ValueError("数字不在有效内")		
	def get_name(self):
		return str(self.__name)
	def get_age(self):
		return int(self.__age)
	def get_course(self):
		return max(self.__c,self.__m,self.__e)
	

s=Student("huang",23,101,90,88)
try:
	print("最高分是：{}".format(s.get_course()))
except ValueError as e:
	print("exception:%s"%e)


















