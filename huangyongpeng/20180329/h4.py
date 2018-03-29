
'''
定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
'''

def hyp(m,n):
	res=0
	l=[]
	count=0
	for i in range(n):
		if i==0:
			res=m
			l.append(res)
			count+=res
		elif i!=0:
			res=res*10+m
			l.append(res)
			count+=res
	print(l)
	print(count)



if  __name__=='__main__':
	a=int(input("请输入第一个整型数："))
	
	b=int(input("请输入第一个整型数："))
	hyp(a,b)
