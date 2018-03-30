"""
电子表工程
００：００：００
七管
用到ｔｕｒｔｌｅ／ｄａｔｅｔｉｍｅ
"""
import turtle as tt
# 画线
def drawLine(isdraw):
	tt.pendown() if isdraw else tt.penup()
	tt.pensize(10)
	tt.forward(40)
	tt.right(90)


# 画数字0 1 2 3 4 5 6 7 8 9
def drawDight(number):
	drawLine(True) if number in (2,3,4,5,6,8,9) else drawLine(False)
	drawLine(True) if number in (0,3,4,5,6,7,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,5,6,8,9) else drawLine(False)
	drawLine(True) if number in (0,1,2,6,8) else drawLine(False)
	tt.left(90)
	
	drawLine(True) if number in (0,1,4,5,6,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,5,6,7,8,9) else drawLine(False)
	drawLine(True) if number in (0,2,3,4,7,8,9) else drawLine(False)
	tt.left(180)
	tt.penup()
	tt.forward(20)
	tt.pendown()
