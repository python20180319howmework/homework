'''计算出100~1000有多少个水仙花数'''
from math import *
count=0
for num1 in range(100,1000):
	l=len(str(num1))
	num2=int(num1)
	num3=num2
	res=0
	while num2>0:
		m=num2%10
		num2//=10
		res+=pow(m,l)
	if res==num3:
		count+=1
print("100到1000之间有%d个水仙花数"%(count))
