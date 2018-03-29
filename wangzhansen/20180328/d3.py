'''
3.定义一个函数，计算给定的整型数是否为质数
'''
def zhi(t):
	for i in range(2,t):
		n = t % i 
		if n == 0:
			print("这不是质数")
			break
	print("这是质数")
y = int(input("请输入一个正整数"))
z = zhi(y)






















