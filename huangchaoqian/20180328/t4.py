'''
定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
'''
def func(m,n):
	a=0
	l=[]
	for i in range(n):
		a=a*10+m
		l.append(a)
#		print(l[i])
	print(l)
	s=0
	for i in l:
		s+=i
	print("以上数的总和是：",s)	
#	print(type(s))
m,n=eval(input('please input two num:'))
func(m,n)

