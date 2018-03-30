


import h4
import turtle


def time11(number):
	for i in number:
		
		if i=="+":
			turtle.write("年",font=("Arial",50,"bold"))
			turtle.penup()
			turtle.forward(80)
			turtle.pendown()
		elif i=="-":
			turtle.write("月",font=("Arial",50,"bold"))
			turtle.penup()
			turtle.forward(80)
			turtle.pendown()
		elif i=="&":
			turtle.write("日",font=("Arial",50,"bold"))
			turtle.penup()
			turtle.forward(80)
			turtle.pendown()
		else:
			h4.drawshuzi(int(i))

if __name__=="__main__":
	turtle.setup(800,400,200,300)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	s=("1995+03-27&")
	time11(s)
	turtle.done()

	

