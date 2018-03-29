"""
3.定义一个函数，计算给定的整型数是否为质数
"""
# 除了１和它本身没有其他因数是质数
def prime(num):
	
	for i in range(2,num):
		if num % i != 0:
			print("{}是质数".format(num))
			break
		else:
			print("{}不是质数！".format(num))
			break

num = int(input("请输入一个整数："))
prime(num)		
		
	
