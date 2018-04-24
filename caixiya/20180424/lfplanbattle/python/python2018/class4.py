class Person(object):
	def __init__(self,name,gender):
		print("init Person is called")
		self.__name=name
		self.__gender=gender

class Student(Person):
	def __init__(self):
		print("init Student is called")
		Person.__init__(self,name,gender,score)
		self.__score=score

class Teacher(Person):
	def __init__(self):
		print("init Teacher is called")
		Person.__init__(self,name,gender,salory)
		self.__salory=salory

class Cadet(Student,Teacher):
	def __init__(self):
		Student.__init__(self,name,gender,score)
		Teacher.__init__(self,name,gender,salory)

c=Cadet()

