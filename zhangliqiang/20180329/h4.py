


#4. 尝试将自己的生日显示在画布，可以配个小心心，尽量字体颜色美观
import datetime
import h4_2
import turtle


def mytime(mytimestr):
	for i in mytimestr:
		if i == '+':
			turtle.color("green")	
			turtle.write('年',font =('Arial', 40, 'normal'))
			turtle.penup()
			
			turtle.forward(60)
			turtle.pendown()
		elif i == '-':
			turtle.color("red")	
			turtle.write('月',font =('Arial', 40, 'normal'))
			turtle.penup()
			turtle.forward(60)
			turtle.pendown()

		elif i == '*':
			turtle.color("pink")	
			turtle.write('日',font =('Arial', 40, 'normal'))
			turtle.penup()
			turtle.forward(60)
			turtle.pendown()
			
			
			
			
			
			turtle.right(90)

			turtle.pendown()

			turtle.color("red","red")
			turtle.begin_fill()

			turtle.backward(223.5)
			turtle.circle(100,-180)


			turtle.penup()
			turtle.goto(275,0)
			turtle.right(180)
			turtle.pendown()

			turtle.backward(223.5)
			turtle.right(180)
			turtle.circle(100,180)
			turtle.end_fill()
			
		else:	
			h4_2.drawDigit(int(i))
		
if __name__=="__main__":
	turtle.setup(800,600,200,200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	s = ('1995+02-13*')
	mytime(s)
	turtle.done()

