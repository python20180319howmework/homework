class Student(object):
	def __init__(self,name,age,*score):
		self.__name = name
		self.__age = age
		self.__score = score
		if not isinstance(self.__name,str):
			raise TypeError("this name is error")
		if not isinstance(self.__age,int):
			raise TypeError("this age is error")
		for i in self.__score:
			if i < 0 or i > 100	:
				raise ValueError("this number is error")
	def get_name(self):
		return self.__name
	def get_age(self):
		return self.__age
	def get_course(self):
		return max(self.__score)

'''
s = Student("zhangsan",18,50,30,60)
print(s.get_name())
print(s.get_age())
print(s.get_course())
'''

if __name__ =='__main__':
	name,age,*score = eval(input("请输入学生姓名，年龄和成绩（语文，数学，英语）："))
	s = Student(name,age,*score)
	print("学生姓名：{}".format(s.get_name()))
	print("学生年龄：{}".format(s.get_age()))
	print("最高分数为：{}".format(s.get_course()))
	
