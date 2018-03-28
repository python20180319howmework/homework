#定义一个函数，计算给定的整型数是否为质数
def zhishu(num):      #定义一个函数判断是不是质数，是返回1，不是返回0
	for i in range(2,num//2+1):
		if num%i == 0:
			return 0
	return 1

n = int(input("请输入你要判断的整型数："))

if zhishu(n)== 0:         # 调用函数
	print ("{}不是质数".format(n))
else:
	print("{}是质数".format(n))




