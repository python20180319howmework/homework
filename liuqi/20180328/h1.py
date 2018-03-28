"""
1.编写一个计时器，將计时结果显示出来

"""
import time
#time1 = int(input("请输入计时时间(s)："))
i = 0
while True:
		t = time.time()
		tl = time.localtime(i)
		time.sleep(0.5)
		ts = time.strftime("%H:%M:%S",tl)
		i += 1
		print("\r{:^3}".format(ts),end="")

