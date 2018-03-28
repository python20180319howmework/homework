'''
随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
'''
from random import *
num= randint(1,1000)
print(num)
l=[]
while num>0:
	l.append(num%2)
	num//=2
else:
	l.reverse()
	print(l)
	
		


	




