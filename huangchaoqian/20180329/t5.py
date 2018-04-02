#使用递归函数，实现求得斐波那契数列的第n项
'''
def func(n):
	l=[0,1]
	while n>=2:
		l[n]=l[n-1]+l[n-2]
		n-=1
	return func(n-1)
if __name__=="main":
	n=int(input("please input n:"))
	print(func(n))	
'''
def func(n):
	if n<1:
		return -1
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return func(n-1)+func(n-2)
if __name__=="__main__":
	n=int(input("please input num n:"))
	for i in range(n+1):
		print(func(i),end=" ")
	print("")
	print("第{}项为{}".format(n,func(n)))
#	print("")




