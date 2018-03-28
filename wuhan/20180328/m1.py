import time 
for i in range(200):
	t = time.localtime(i)
	t1 = time.strftime("%s",t)
	print("\r{}秒".format(t1),end = "")
	time.sleep(1)
