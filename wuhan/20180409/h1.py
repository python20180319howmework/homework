class Student(object):
	def __init__(self,name,age,chinese,math,english):
		self._name = name
		self._age = age
		self._chinese = chinese
		self._math = math
		self._english = english
		if self._chinese < 0 or self._chinese > 100 or self._math < 0 or self._math > 100 or self._english < 0 or self._english >100:
			raise ValueError('数字不在0~100以内')
	def get_name(self):
		return str(self._name)
	def get_age(self):
		return int(self._age)
	def get_course(self):
		return max(self._chinese,self._math,self._english)

s = Student('wuhan',21,100,0,59)
try:
	print(s.get_course())
except ValueError as e:
	print('exception: %s' % e)
	 
