#定义一个函数，计算给定的整型数是否为质数
def func():
	n=int(input('please input num:'))
	if n>=2:
		for i in range(2,n//2+1):
			if n%i==0:
				print("{}不是质数".format(n))
				break
		else:
			print("{}是质数".format(n))
	else:
		print("{}不是质数".format(n))
func()
