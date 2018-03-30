import datetime
import l4  as mye
import turtle 


def mytime(*mytimestr):
	for i in mytimestr:
		mye.drawDigit(int(i))
   # mye.drawnum(i)
if __name__ == "__main__":
	turtle.setup(1200, 1000, 200, 200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()	
	mytime(1,9,9,4,0,9,2,7)
	turtle.pensize(6)
	turtle.speed(8)
	turtle.circle(-80,182)
	turtle.forward(100)
	turtle.left(300)
	turtle.forward(100)
	turtle.circle(-80,182)
	turtle.done()
