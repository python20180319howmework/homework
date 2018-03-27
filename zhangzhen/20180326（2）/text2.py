
#随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
from random import *
#随机一个正整数
myint = randint(0,100)
print(myint)
#求二进制
#定义一个列表
l = []
for i in range(0,50):
	if myint > 1:
		newmyint = myint % 2
		myint = myint //2
		i += 1
		l.insert(0,newmyint)
else:
	l.insert(0,myint)
print(l)
	



