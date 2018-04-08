'''
定义一个学生类,有下面的类属性:
1 姓名
2 年龄
3 成绩(语文,数学,英语)(每课成绩类型为整型)
类方法:
1 获取学生的姓名:get_name()返回类型:str
2 获取学生的年龄:get_age()返回类型:int
3 返回3门科目中最高的分数.get_course()返回类型
要求成绩如果不在0到100抛出ValueError
'''
class Xuesheng(object):
	def __init__(self, age = 23 , yuwen = 60 , shuxue = 60 , yingyu = 60 ):
	
		self._age = age
		self._yuwen = yuwen
		self._shuxue = shuxue
		self._yingyu = yingyu
	def course(self, zuigao):
		self._yuwen = yuwen
		self._shuxue = shuxue
		self._yingyu = yingyu
		if self._yuwen > self._shuxue > self._yingyu:
			self._zuigao = self._yuwen
		elif self._shuxue >self._yingyu:
			self._zuigao = self._shuxue
		else:
			self._zuigao = self._yingyu
		print(self._zuigao)
l = int(input("请输入年龄和三科成绩:")
l.course()































