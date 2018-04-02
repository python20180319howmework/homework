"""
4. 尝试将自己的生日显示在画布，可以配个小心心，尽量字体颜色美观
"""
import watch_2 as my
import watch_1 as mye
import turtle 
def mytime(mytimestr):
	for i in mytimestr:
		
		mye.drawDight(int(i))
def curvemove():
    for i in range(200):
       turtle.right(1)
       turtle.forward(1)
	
if __name__ == "__main__":
	
	turtle.setup(800, 600, 200, 200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	#获取当前年月日

	s =str(19940401)
	mytime(s)
	turtle.penup()
	turtle.left(10)
	turtle.forward(100)
	turtle.pendown()
	turtle.color("red","pink")
	turtle.begin_fill()
	turtle.left(140)
	turtle.forward(111.65)
	curvemove()
	turtle.left(120)
	curvemove()
	turtle.forward(116.5)
	turtle.end_fill()
	turtle.done()


