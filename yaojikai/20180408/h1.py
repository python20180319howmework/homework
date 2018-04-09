
'''
定义一个学生类。有下面的类属性：
1姓名
2年龄
3成绩（语文，数学，英语）[每课成绩的类型为整数]
类方法：
1获取学生的姓名：get_name()
2获取学生的年龄：get_age()返回类型int
3返回3门科目中最高得分数。
get_course()返回类型
要求：成绩如果不在0到100抛出ValueError

'''

class Student(object):
	
	def __init__(self,name,age,*cour):
		self._name = name
		self._age = age
		self._cour = cour
		for i in self._cour:
			if not 0<i<100:
				raise ValueError("输的不对")

	def get_name(self):
		print("姓名：{}".format(self._name))
	
	def get_age(self):
		print("年龄：{}".format(int(self._age)))

	def get_course(self):
		return max(self._cour)
s = Student("zhangsan",18,11,12,10)
s.get_name()
s.get_age()

print("最高成绩：{}".format(s.get_course()))


