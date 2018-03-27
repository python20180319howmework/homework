#编写一个计时器,将计时结果显示出来
import time

print("计时:")

for i in range(200):
	t = time.localtime(i)
	tl = time.strftime("%s",t)
	print("\r{}秒".format(tl),end = "")
	time.sleep(1)
