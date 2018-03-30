


import turtle as tt


def drawLine(isdraw):
	tt.pendown()if isdraw else tt.penup()
	tt.pensize(5)
	tt.color("blue")
	tt.forward(40)
	tt.right(90)

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
	tt.fd(10)
	
	tt.pendown()
