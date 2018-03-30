#尝试将自己的生日显示在画布，可以配个小心心，尽量字体颜色美观
import turtle
def drawline(isdraw):
	turtle.pendown() if isdraw else turtle.penup()
	turtle.color("yellow","red")
	turtle.begin_fill()
	turtle.pensize(5)
	turtle.forward(40)
	turtle.right(90)
	turtle.end_fill()

def drawDigit(num):
	drawline(True) if num in (2,3,4,5,6,8,9)	else drawline(False)
	drawline(True) if num in (0,1,3,4,5,6,7,8,9) else drawline(False)
	drawline(True) if num in (0,2,3,5,6,8,9)	else drawline(False)
	drawline(True) if num in (0,2,6,8)	else drawline(False)
	turtle.left(90)

	drawline(True) if num in (0,4,5,6,8,9)	else drawline(False)
	drawline(True) if num in (0,2,3,5,6,7,8,9)	else drawline(False)
	drawline(True) if num in (0,1,2,3,4,7,8,9)	else drawline(False)
	turtle.left(180)

	turtle.penup()
	turtle.fd(20)
	turtle.pendown()

def my_datetime(mytime):
	for i in mytime:
		drawDigit(int(i))

if __name__=="__main__":
	s=input("please input your birthday:")
	turtle.setup(800,600,200,200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()

#	s=input("please input your birthday:")
	my_datetime(s)
	turtle.done()


