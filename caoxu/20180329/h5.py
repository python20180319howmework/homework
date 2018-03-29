'''
使用递归函数，实现求得斐波那契数列的第n项
'''


def mysum(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return mysum(n-1)+mysum(n-2)


if __name__ =='__main__':
	n = int(input("输入所求项:"))
	print("第{}项的值为{}".format(n,mysum(n)))
