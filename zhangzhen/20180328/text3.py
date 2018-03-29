
#定义一个函数，计算给定的整型数是否为质数

#除了1 和它 本身 没有其他因数
#储存给定的数
num = int(input("请输入一个整型数："))

#定义一个函数
def zhishu(num):
	for i in range(2,num):
		if (num%i)== 0:
			print(num,"不是质数")
			break
	else:
		print(num,"是质数")
		return num
#调用
print(zhishu(num))










