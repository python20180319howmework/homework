import math


class Student(object):
	
	def __init__(self,name="liqiang",age=23,*score):
		self.__name = name
		self.__age = age
		self.__score = score
	def get_name(self):
		return self.__name
	def get_age(self):
		return self.__age
	
	def score(self):
		return self.__score
	
	def score(self, value1,value2,value3):
		if not isinstance(value,int):
			raise ValueError("类型必须为整数")
		
		elif  value< 0 or value > 100:
			raise ValueError("成绩应为0-100之间")
		else:
			return  max(*score)
				
	def pri_stu(self):
		print("学生名字为{}年龄为{}最高成绩为{}".format(self.__name,self.__age,self.__score))

s1 = Student("sd",22,88,77,99)
s1.pri_stu()



