#使用递归函数，实现求得斐波那契数列的第n项
def func(n):
	l=[0,1]
	while n>=2:
		l[n]=l[n-1]+l[n-2]
		n-=1
	return l[n]

if __name__=="main":
	n=int(input("please input n:"))
	print(func(n))	

