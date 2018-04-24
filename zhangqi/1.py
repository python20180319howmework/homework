'''
一：定义一个学生类。有下面的类属性：
1 姓名  2 年龄  3成绩（语文，数学，英语）（每课成绩的类型为整数）
类方法：
1 获取学生的姓名：get_name() 返回类型：str
2 获取学生的年龄： get_age() 返回值类型:int
3 返回3们科目中最高的分数: get_course() 返回类型
要求： 成绩如果不在0到100跑出ValueError



二. 定义一个列表的操作类： Listinfo
包括方法：
	1   列表元素添加：add——key（keyname）[keyname:字符串或者整型数类型]
	2	列表元素取值： get_key(num)[num:整数类型]
	3	列表合并:update_list(list)[list:列表类型]
	4	删除并且返回最后一个元素： del_key()
'''
class Stu(object):
	print("this is a debug")
	def __init__(self, name, age, *grade):
		self.__name = name
		self.__age = age
		self.__grade = grade
	def get_name(self):
		return str(self.__name)
	def get_age(self):
		return int(self.__age)
	def get_course(self):
		for i in self.__grade:
			if i > 100 or i < 0 :
				return ("ValueError")
	
		return max(self.__grade)
a = Stu("ab",23,60,66,59)
print(a.get_name())
print(a.get_age())
print(a.get_course())
		








