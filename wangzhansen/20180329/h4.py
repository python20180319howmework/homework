
import datetime
import e3293_module as mye
import turtle

def mytime(mytimestr):
	for i in mytimestr:
		if i == "+":
			turtle.write("年",font=('Arial', 20, 'normal'))
			turtle.penup()
			turtle.forward(40)
			turtle.pendown()
		elif i == "-":
			turtle.write("月",font=('Arial', 20, 'normal'))
			turtle.penup()
			turtle.forward(40)
			turtle.pendown()
		elif i == "#":
			turtle.write("日",font=('Arial', 20, 'normal'))
			turtle.penup()
			turtle.forward(40)
			turtle.pendown()
		else:
			mye.drawDigit(int(i))

if __name__ == "__main__":
	turtle.setup(1000 , 600 , 200 , 300)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown

	#获取当前的年月日	
	s = datetime.date.strftime(datetime.datetime.now(), "%Y+%m-%d#")
	mytime(s)

	turtle.done()































