'''
尝试将自己的生日显示在画布，可以配个小心心，尽量字体颜色美观
'''

import datetime
import turtle as tt

# 画数字管

# 画线
def drawLine(isdraw):
	tt.pendown() if isdraw else tt.penup()
	tt.pensize(5)
	tt.forward(40)
	tt.right(90)

# 画数字 0 1 2 3 4 5 6 7 8 9
def drawDigit(number):
	drawLine(True) if number in (2,3,4,5,6,8,9)	else drawLine(False)
	drawLine(True) if number in (0,3,4,5,6,7,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,5,6,8,9) else drawLine(False)
	drawLine(True) if number in (0,1,2,6,8) else drawLine(False)
	tt.left(90)
	drawLine(True) if number in (0,1,4,5,6,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,5,6,7,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,4,7,8,9) else drawLine(False)
	tt.left(180)
	tt.penup()
	tt.fd(20)
	tt.pendown()


def mytime(mytimestr):
	for i in mytimestr:
		if i=='+':
			tt.write('年',font=('Arial', 40, 'normal'))
			tt.penup()
			tt.fd(80)
			tt.pendown()
		elif i=='-':
			tt.write('月',font=('Arial', 40, 'normal'))
			tt.penup()
			tt.fd(80)
			tt.pendown()
		elif i=='*':
			tt.write('日',font=('Arial', 40, 'normal'))
			tt.penup()
			tt.fd(40)
			tt.pendown()
		else:	
			drawDigit(int(i))	
		





if  __name__ == "__main__":
	tt.setup(800, 600, 200, 200)
	tt.penup()
	tt.backward(300)
	tt.pendown()
	
	# 获取当前的年月日
	s = "1994+12-25*"
	mytime(s)
	tt.penup()
	tt.goto(0,100)
	tt.pendown()
	tt.begin_fill()
	tt.color("red")
	tt.left(40)
	tt.fd(80)
	tt.circle(40,200)
	tt.right(110)
	tt.circle(40,200)
	tt.fd(80)
	tt.end_fill()
		
	tt.done()

