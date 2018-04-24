from enum import Enum

week=Enum('WEEK',("Mon","Tues","Wed","Thur","Fri","Sat","Sun"))
for name,member in week.__members__.items():
	print(name,member,member.value)

class Week(Enum):
	Sun=0
	Mon=1
	Tues=2
	Wed=3
	Thur=4
	Fir=5
	Sat=6

print(Week.Sun)
print(Week.Sun.value)
print(Week['Wed'].value)
print(Week(6))

import time
class Fib(object):
	def __init__(self):
		self._a=0
		self._b=1
	def __iter__(self):
		return self
	def __next__(self):
		self._a,self._b=(self._b,self._a+self._b)
		while self._a>1000:
			raise StopIteration()
		return self._a
f=Fib()
for i in f:
	print(i)
	time.sleep(0.1)

def saysth(word="good"):
	print("hello,%s"% word)
class Mydef():
	def mymethod(self):
		pass
type('Mydef',(object.),dic(mymethod=saysth))
m=Mydef()
print(m.mymethod)
