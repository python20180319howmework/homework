
'''
定义一个学生类（name,age,score(Chinese,Math,English)）
成绩为整数
类方法
获取学生姓名get_name   返回值为str 
获取学生年龄get_age   返回值为int
返回3 门中分数最高的get_course
'''

class Student(object):
	def __init__(self,name,age,course):
		self.__name = name
		self.__age = age 
		self.__course = course

		for s in self.__course:
			if s <1 or s >100:       
				raise ValueError("the course is wrong")
	def get_name(self):
		return str(self.__name)
	def get_age (self):
		return int(self.__age)
	def get_course(self):
		return(max(self.__course))

s  = Student("zz",22,[60,61,62])
print("姓名是：{}，年龄是：{}，最高成绩是：{}".format(s.get_name(),s.get_age(),s.get_course()))

































