import datetime
import m2 as mye
from turtle import *
from time import sleep

def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  #函数用于绘制心的大圆
   speed(2000)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
   speed(2000)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
   speed(500)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   speed(6)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(140)

def arrowHead():
   pensize(1)
   speed(50)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()


def mytime(mytimestr):
	for i in mytimestr:
		if i =='+':
			write("年",font = ('Arial',20,'normal'))
			penup()
			fd(80)
			pendown()
		elif i =='-':
			write("月",font = ('Arial',20,'normal'))
			penup()
			fd(80)
			pendown()
		elif i =='*':
			write("日",font = ('Arial',20,'normal'))
			penup()
			fd(40)
			pendown
		else:	
			mye.drawDigit(int(i))

def main():
   pensize(2)
   color('red', 'pink')
   #getscreen().tracer(30, 0) #取消注释后，快速显示图案
   heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置
   setheading(0)             #使画笔的方向朝向x轴正方向
   heart(-80, -100, 1.5)     #画出第二颗心
   arrow()                   #画出穿过两颗心的直线
   arrowHead()               #画出箭的箭头
   done()
	
	
if __name__ == "__main__":
	setup(1500, 1300, 100, 100)
	penup()
	backward(300)
	right(90)
	fd(100)
	left(90)
	pendown()
	
	# 获取当前的年月日
	s = "2018+03-29*"
	mytime(s)
	main()
	
