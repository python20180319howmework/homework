
#水仙花数
from math import *
'''
num=int(input("输入三位整形数："))
baiwei=num//100
shiwei=(num//10)%10
gewei=num%10
count=0
if num==baiwei*baiwei*baiwei+shiwei*shiwei*shiwei+gewei*gewei*gewei:
	print("{}是水仙花数".format(num))
	
else:
	print("{}不是水仙花数".format(num))
	
print(count)
'''




for i in range(100,1000):
	baiwei=i//100
	shiwei=(i//10)%10
	gewei=i%10
	if i==baiwei*baiwei*baiwei+shiwei*shiwei*shiwei+gewei*gewei*gewei:
		print(i,end=",")
		
	

