#随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
import random
#import string
n=random.randint(1,1000)
print(n)
l=[]
while n!=0:
	a=n%2
	b=n//2
	l.append(str(a))
	n=b
l.reverse()
a="".join(l)
#print(type(a))
print(int(a))
