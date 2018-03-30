'''
	编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
'''


def func(*num,base = 3):
	res = 0
	for i in num:
		res += i
	return res * base



if __name__ =='__main__':
	
	print(func(1,2,3,4,base=1))
	print(func(1,2,3,4))
