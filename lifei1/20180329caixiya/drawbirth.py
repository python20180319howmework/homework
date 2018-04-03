import datetime
import draw 
import turtle as tt

def drawmybirth(mybirthstr):
	for i in mybirthstr:
		draw.drawDigit(int(i))

if __name__ == "__main__":
	tt.setup(800, 600, 200, 200)
	tt.penup()
	tt.backward(300)
	tt.pendown()
	
	# 画生日
	drawmybirth("19960324")
	#画小心心
	tt.pensize(6)
	tt.speed(8)
	tt.fillcolor=("red")
	tt.begin_fill()
	tt.circle(-80,120)
	tt.forward(100)
	tt.left(300)
	tt.forward(100)
	tt.circle(-80,120)
	tt.end_fill()
	tt.done()
