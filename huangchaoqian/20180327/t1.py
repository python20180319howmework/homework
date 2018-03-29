#编写一个计时器,将计时结果显示出来
import time
#tl=time.localtime()
for i in range(100):
	tl=time.localtime()
	ts=time.strftime("%H:%M:%S",tl)
	print(ts,end="\r")
	time.sleep(1)

