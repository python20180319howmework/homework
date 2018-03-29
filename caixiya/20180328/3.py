'''
定义一个函数，计算给定的整型数是否为质数
'''
def isprime(num):
	if num>=2:
		for i in range(2,num//2+1):
			if(num%i==0):
				return False
			else:
				return True
		else:
			#print("{}是质数".format(num))
			return True
	else:
		#print("{}不是质数".format(num))
		return False
num=int(input("请输入一个整型数："))
if isprime(num):
	print("{}是质数".format(num))
else:
	print("{}不是质数".format(num))
