'''
1.定义一个学生类,属性:姓名,年龄,成绩(语文,数学,英语)
方法:
    1.获取学生的姓名
    2.获取年龄
    3.三门成绩的最高分
成绩在0-100之间，否则要抛出异常
'''
class Student(object):
	def __init__(self, name, age, score):
		self.__name=name
		self.__age=age
		self.__score=score
		for s in self.__score:
			if s < 0 or s > 100:
				raise ValueError("你的每一科成绩必须在0到100之间")
	def getName(self):
		return self.__name
	def getAge(self):
		return self.__age
	def getMaxScore(self):
		return max(self.__score)

s = Student("zhangshile", 20, [90, 89, 100])
print("{} age:{},学的最好的一门成绩:{}".format(s.getName(), s.getAge(), s.getMaxScore()))
try:
	s2 = Student("zhangshile", 18, [90, -89, 100])
	print("{} age:{},学的最好的一门成绩:{}".format(s2.getName(), s2.getAge(), s2.getMaxScore()))
except ValueError as e:
	print("程序出现异常:%s" % e)

print("结束了")

