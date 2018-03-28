#随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
import random

s = random.randint(1,100)
print("s=%d"%(s))

l = []
count = 0

while s>0:
	for i in range(8):
		l.append(s%2) 
		s //= 2
		count += 1
else:
	print("对应的二进制为:",end="")
for i in range(count):
	print(l[count-i-1],end="")
