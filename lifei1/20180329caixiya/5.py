'''
使用递归函数，实现求得斐波那契数列的第n项
'''
def sumn(n):
	summ1=0
	if n==0:
		summ1=0
	if n==1:
		summ1=1
	if n>=2:
		summ1=summ1+sumn(n-1)+sumn(n-2)
	return summ1
if __name__=="__main__":
	n=int(input("请输入第几项："))
	print("斐波那契数列的第{}项是{}".format(n,sumn(n)))
