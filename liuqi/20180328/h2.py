"""
2.随机产生一个正整数，不要使用python内置方法，求得其二进制表达，并输出
"""
from random import randint
num = randint(10,20)
print(num)
list1 = []
num1 = 0
while True:
	num1 = num % 2
	list1.append(num1)
	num = num//2
	if num == 0 :
		break
print(list1)
list2 =list1[::-1]
	
print("改变二进制是：{}".format(list2)) 