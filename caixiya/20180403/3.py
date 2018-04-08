'''
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

游戏背景大小 x(0-10) y(0-10)
乌龟1只,左移1 左移2 右移1 右移2 上移1 上移2 下移1 下移2 
x龟=[-1,-2,1,2] y龟=[1,2,-1,-2]random.randint()
当移动到x=0 or 10 y=0 or 10 时自动反向
龟100 -1/次 （x龟，y龟）=（x鱼，y鱼）龟+10
龟=0 print("小样！还想吃我")

小鱼5条 左移1 右移1 上移1 下移1 x鱼=[-1,1] y鱼=[1,-1]
鱼没有了 print("哈哈哈哈！敢惹我龟丞相")
'''
import random

class Turtlet(object):
	def __init__(self,position,power):
		self.position=[5,5]
		self.power=power
		#if self.d=="left"
			#self.position[0]-=1
		lxg=[-1,-2,1,2]
		lyg=[1,2,-1,-2]
		nx=random.sample(lxg,1)
		ny=random.sample(lyg,1)
		self.position=[self.position[0]+nx,self.position[1]+ny]
		if self.position[0]==0 or self.position[1]==10:
			
class Fish(object):
	def __init__(self,xf,yf):
		self.xf=xf
		self.yf=yf
g=Turtlet()
f1=Fish()
f2=Fish()
f3=Fish()
f4=Fish()
f5=Fish()

