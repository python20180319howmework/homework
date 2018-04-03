#4. 尝试将自己的生日显示在画布，可以配个小心心，尽量字体颜色美观
import turtle as tt

# 画数字管

# 画线
def drawLine(isdraw):
	tt.pendown() if isdraw else tt.penup()
	tt.pensize(5)
	tt.forward(35)
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
	tt.fd(15)
	tt.pendown()


import datetime
import turtle

def mytime(mytimestr):
	for i in mytimestr:
		if i == "*":
			turtle.write("年", font=('Arial', 50, 'normal'))
			turtle.penup()
			turtle.fd(50)
			turtle.pendown()
		elif i == "-":
			turtle.write("月", font=( 'Arial',50, 'normal'))
			
			turtle.penup()
			turtle.fd(50)
			turtle.pendown()
		elif i == "+":
			turtle.write("日", font=('Arial', 50, 'normal'))
		else: 
			drawDigit(int(i))

if __name__ == "__main__":
	turtle.setup(800, 600, 200, 200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	
	# 获取当前的年月日
	s = ("1994*11-15+")
	mytime(s)
	tt.hideturtle()
	turtle.done()
	





























