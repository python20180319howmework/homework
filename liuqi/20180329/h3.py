"""
3.定义一个函数，计算给定的整型数是否为质数
"""
# 除了１和它本身没有其他因数是质数,1和０不是质数也不是合数
def prime(num):

	if num ==0 and num ==1:
		return -1	
	for i in range(2,num//2+1):
		if num % i == 0:  

 # 这里取模只能等于零，因为如果不等于零，只需要有一项取模不等于零就会返回值１
			return 1
	
	return 0
 
if __name__ == "__main__":
	n = int(input("请输入一个整数："))
		
	if prime(n) == 1:
		print("{}不是质数".format(n))
	elif prime(n)== 0:		
		print("{}是质数！".format(n))
	else:
		print("{}既不是素数也不是合数".format(num))
