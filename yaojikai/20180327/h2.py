#2,随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
import random

l = []

num = random.randint(1,100)
numb = num

for i in range(100):
	if num > 0:
		res = num % 2
		num//=2
		l.append(res)

l.reverse()

print("随机生成的正整数为{},它的二进制表达是{}".format(numb,l))









