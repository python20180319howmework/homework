'''
使用递归函数，实现求得斐波那契数列的第n项
0 1 1 2 3 5 8 13 
1 2 3 4 5 6 7 8
'''
def digui(n):
	l=[]
	for i in range(n):
		if i ==0  :
			l.append(0)
		elif i==1:
			l.append(1)
		else:
			l.append(l[i-2]+l[i-1])
	return l[n-1]


if __name__=="__main__":
	k=int(input("请输入n值："))
	
	print(digui(k))

