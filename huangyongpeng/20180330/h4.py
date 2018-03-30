




import turtle as tt


def drawline(p):
	tt.pendown() if p else tt.penup()
	tt.pensize(5)
	tt.forward(40)
	tt.right(90) 
#0123456789
def drawshuzi(number):
	drawline(True) if number in (2,3,4,5,6,8,9)  else drawline(False)
	drawline(True) if number in (0,3,4,5,6,7,8,9) else drawline(False) 
	drawline(True) if number in (0,2,3,5,6,8,9) else drawline(False)
	drawline(True) if number in (0,1,2,6,8) else drawline(False)
	tt.left(90)
	drawline(True) if number in (0,1,4,5,6,8,9)  else drawline(False)
	drawline(True) if number in (0,2,3,5,6,7,8,9) else drawline(False)
	drawline(True) if number in (0,2,3,4,7,8,9) else drawline(False)
	tt.left(180)
	tt.penup()
	tt.forward(20)
	tt.pendown()
	

