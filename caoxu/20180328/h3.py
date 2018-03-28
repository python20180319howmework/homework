#定义一个函数，计算给定的整型数是否为质数
def number(n):
	if n <= 1:
		print("error")
	elif n == 2 or n==3:
		return 1
	else:
		for i in range(2,((n//2)+1)):
			if n%i != 0:
				return 1
			else:
				return 0


if __name__ == '__main__':
	l = int(input("输入一个整型数:"))
	s = number(l)
	if s:
		print("{}是质数".format(l))
	else:
		print("{}不是质数".format(l))
