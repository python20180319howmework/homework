#1,编写一个计时器,将计时结果显示出来

import time

for i in range(100):
	print("\r 当前的时间是{}".format(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(time.time()))),end='')
	time.sleep(1)

