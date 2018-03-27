'''输入一个三位整型数，判断它是否是一个水仙花数(比如153 = 1*1*1 + 5*5*5 + 3*3*'''
from math import *
num1=input("输入一个三位整型数:")
l=len(num1)
num2=int(num1)
num3=num2
res=0
while num2>0:
	m=num2%10
	num2//=10
	res+=pow(m,l)
if res==num3:
	print("是水仙花数")
else:
	print("不是水仙花数")
