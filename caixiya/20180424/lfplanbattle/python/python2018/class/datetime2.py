import datetime
import datetime1 as mye
import turtle


def mytime(mytimestr):
	for j in range(len(mytimestr)):
		for i in mytimestr:
			mye.drawDigit(int(i))
			if j==4:
				turtle.write("年")
			if j==6:
				turtle.write("月")
			if j==8:
				turtle.write("日")

if __name__ == "__main__":
	turtle.setup(800, 600, 200, 200)
	turtle.penup()
	turtle.backward(300)
	turtle.pendown()
	
	# 获取当前的年月日
	s = datetime.date.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
	mytime(s)
	
	turtle.done()
	
