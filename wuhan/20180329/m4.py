def emmm(a,b):
	res=0
	l=[]
	count=0
	for i in range(b):
		if i==0:
			res=a
			l.append(res)
			count+=res
		elif i!=0:
			res=res*10+a
			l.append(res)
			count+=res
	print(l)
	print(count)

if  __name__=='__main__':
	m=int(input("请输入第一个整数："))
	
	n=int(input("请输入第二个整数："))
	emmm(m,n)	
	
