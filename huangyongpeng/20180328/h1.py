
from time import *
for i in range(100):
	print(strftime("\r%H:%M:%S",localtime(time())),end="")
	
	sleep(1)


