#编写一个计时器,将计时结果显示出来

#引入time 方法
import time

mytime = int (input("请输入您需要的计时时间："))
for i in range(0,mytime):
#时间延迟
	time.sleep(1)
# 时间戳
	#t =- time.time()

#把时间戳转换成时间结构
	tl = time.localtime()
#转换时间字符串
	ts = time.strftime("%H:%M:%S",tl)
	print("\r{:}".format(ts),end = '')
	i += 1
else:
	pass
print("")






