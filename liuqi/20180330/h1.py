"""
1. 编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
"""
def mysum(base=3,*arg):
	sum_1 = 0
	for i in arg:
	
		sum_1 += i
	sum_2  = sum_1 * base
	return sum_2

if __name__ == "__main__":
	
	num1,num2,num3,num4 = 1,2,3,4
	a = mysum(num1,num2,num3,num4)
	print(a)

    
	
