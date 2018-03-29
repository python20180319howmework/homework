



#3.定义一个函数，计算给定的整型数是否为质数
def zhishu(num):
	for i in range(2,num//2+1):
		if num % i == 0:
			return 0
	return 1
n = int(input("请输入一个整形数"))
if zhishu(n)== 0 :

	print("{}不是一个质数".format(n))
else:
	print("{}是质数".format(n))				



