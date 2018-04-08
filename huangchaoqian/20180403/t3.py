from random import randint
class Turtle():
	def __init__(self,value=100)
		self.__value=value
	def movestep(self):
		return randint(1,2)
	def addvalue(self):
		return self.__value+=10
	def subvalue(self):
		return self.__value-=1

class Fish():
	def __init__(self,num=5):
		self.__num=num
	def movestep(self):
		return 1
	def subnum(self,num):
		return self.__num-=1

def location(tx,ty,fx,fy):
	flag=0
	if tx==fx:
		if ty==fy:
			flag=1
	return flag
		                                               
def gamefinish(t,f):
	if t=0:
		print("game over!  fish:小样！还想吃我")
	if f=0:
		print("turtle:哈哈哈！敢惹我龟丞相")



