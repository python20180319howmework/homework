#1. 编写一个函数：
#   1) 计算所有参数的和的基数倍(默认基数为base=3
def sumnum(*a,b=3):
	sum1 = 0
	for i in a:
		sum1 = sum1 + i
		sum2 = pow(sum1,b)
	print(sum2)
sumnum(1,2,3,4)




















