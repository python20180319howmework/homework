'''
.模拟一个乌龟吃小鱼的游戏
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



'''
import random
class Turtle(object):
	def __init__(self):
		self.__tili=100
		self.__x=random.randint(0,10)
		self.__y=random.randint(0,10)
	def yidong(self):
		self.__bushu=random.randint(1,2)
		self.__hl=self.__tili-self.__bushu
	def fangxiang(self):
		self.__fx=random.randint(1,4)
		return self.__fx
	def weizhi(self):
		if self.__fx==1:
			self.__newx=self.__x+self.__bushu
			if self.__newx>10:
				self.__newx=self.__newx-(self.__newx-10)
			self.__newy=self.__y
		elif self.__fx==2:
			self.__newx=self.__x-self.__bushu
			if self.__newx<0:
				self.__newx=self.__newx+(0-self.__newx)
			self.__newy=self.__y
		elif self.__fx==3:
			self.__newy=self.__y+self.__bushu
			if self.__newy>10:
				self.__newy=self.__newy-(self.__newy-10)
			self.__newx=self.__x
		else:
			self.__newy=self.__y-self.__bushu
			if self.__newy<0:
				self.__newy=self.__newy+(0-self.__newy)
			self.__newx=self.__x
	def tineng(self):
		pass	
	def showb(self):
		print("乌龟当前位置是（{}，{}）".format(self.__x,self.__y))
		print("乌龟移动了{}步".format(self.__bushu))
		print("乌龟当前还有{}体力".format(self.__hl))
		print("乌龟移动后位置是（{}，{}）".format(self.__newx,self.__newy))
class Yu(object):
	def __init__(self):
		self.__m=random.randint(1,10)
		self.__n=random.randint(1,10)
	def fangxiang2(self):
		self.__fx2=random.randint(1,4)
	def weizi2(self):
		if self.__fx2==1:
			self.__newm=self.__m+1
			if self.__newm>10:
				self.__newm=self.__newm-(self.__newm-10)
			self.__newn=self.__n
		elif self.__fx2==2:
			self.__newm=self.__m-1
			if self.__newm<0:
				self.__newm=self.__newm+(0-self.__newm)
			self.__newn=self.__n
		elif self.__fx2==3:
			self.__newn=self.__n+1
			if self.__newn>10:
				self.__newn=self.__newn-(self.__newn-10)
			self.__newm=self.__m
		else:
			self.__newn=self.__n-1
			if self.__newn<0:
				self.__newn=self.__newn+(0-self.__newn)
			self.__newm=self.__m	
	
	def showy(self):
		print("小鱼当前位置是（{}，{}）".format(self.__m,self.__n))
		print("移动后小鱼的位置是（{}，{}）".format(self.__newm,self.__newn))


t=Turtle()
t.yidong()
t.fangxiang()
t.weizhi()
t.showb()
q=Yu()
q.fangxiang2()
q.weizi2()
q.showy()

	


