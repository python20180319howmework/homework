'''
编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
'''
import random
def mysum(base=3,*m):
	s=0
	for i in m:
		s+=i
	s=s*base
	return s
if __name__=="__main__":
	l=[]
	n=int(input("please input sum of num:"))
	for i in range(n):
		l.append(random.randint(0,1000))
	print(l)
	base=3
	print(mysum(base,*l))#不带参数，base=l[0],带参数，运算正常
	print(l)
	print(mysum(2,*l))
		 
