"""
3.模拟一个乌龟吃小鱼的游戏
    假设游戏背景在x * y的范围内进行(0<=x<=10, 0<=y <=10)
    游戏中有1只乌龟和5条小鱼
    它们移动的方向是随机的
    乌龟每移动一次可能是1或者2(随机的),小鱼每次就移动1
    当移动的游戏背景边缘,自动向反方向移动
    乌龟的初识体能值是100
    乌龟每移动一次,体能值-1
    小鱼不增加也不消耗体能
    当乌龟和小鱼坐标重叠,就算乌龟吃掉已知小鱼,乌龟的体能值立即上升10
    当乌龟体能为0时,则乌龟死掉,game over,群鱼嘲笑"小样!还想吃我"
    如果小鱼全部被吃掉,游戏也结束!乌龟大笑"哈哈哈哈!敢惹我龟丞相"
    
提示:
    先定义乌龟类和鱼类,将乌龟和鱼类的所有的属性和方法先约定好   
"""

from random import randint
#定义乌龟类
init_x = [0,10]
init_y = [0,10]
class Myturtle(object):
  	
	def __init__(self):
		self.__blood = 100
		self.__tx    = randint(init_x[0],init_x[1])
		self.__ty    = randint(init_y[0],init_y[1])

	def climt(self):
		newtx = self.__tx + random.choice([1,2,-1,-2])
		ty = self.__ty + random.choice([1,2,-1,-2])
		if self.__tx < init_x[0] :	
			self.__tx = init_x[0] - (newtx -init_x[0])
		elif self.__tx > init_x[1] :	
			self.__tx = init_x[1] - (newtx -init_x[1])
		else:
			self.__tx = newtx
		if self.__ty < init_y[0] :	
			self.__ty = init_y[0] - (newty -init_y[0])
		elif self.__ty > init_x[1] :	
			self.__ty = init_y[1] - (newty -init_y[1])
		
		else:
			self.__ty = newty
		self,___blood -= 1
		return (self.__tx,self.__ty)
	def eat(self):
		self.__blood += 10
	def getblood(self):
		return self.__blood



class Myfish(object):
	def __init__(self)
		self.__fx    = randint(init_x[0],init_x[1])
		self.__fy    = randint(init_y[0],init_y[1])
	def swim(self)
		newfx = self.__fx + random.choice([1,-1])
		newfy = self.__fy + random.choice([1,-1])
		if self.__fx < init_x[0] :	
			self.__fx = init_x[0] - (newfx -init_x[0])
		elif self.__fx > init_x[1] :	
			self.__fx = init_x[1] - (newfx -init_x[1])
		else:
			self.__fx = newfx
		if self.__fy < init_y[0] :	
			self.__fy = init_y[0] - (newfy -init_y[0])
		elif self.__fy > init_x[1] :	
			self.__fy = init_y[1] - (newfy -init_y[1])
		
		else:
			self.__ty = newfy
		return (self.__fx,self.__fy)
		
t =Myturtle()

fish = []

for i in range(1,6):
	fish.append(fish())
while True:
	if not len(fish):
		print("dddddd")
		break
	if not t.getblood():
		print("qqqq")
		break
	pos = t.climt()
	for each_fish in fish:
		posf = each_fish.swim
		if each_fish.climt == pos
			print("qwer")
			t.eat()
			fish.swim(each_fish)











