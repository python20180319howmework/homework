

#1. 编写一个函数：
#1) 计算所有参数的和的基数倍(默认基数为base=3)


def mysum(*number):
	res = 0
	for i in number:
		res += i
	return res
	
	



def bei(a,base=3):
	r = 0 
	r = mysum(a) * base
	return r

if __name__=="__main__":
		
	print(bei(mysum(1,3,5)))

		
