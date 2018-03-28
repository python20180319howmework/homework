'''定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)'''


def adc(m,n):
	count = 0
	res = 0
	l=[]
	for i in range(n):
		count = count*10+m
		l.append(count)
	print(l)
	for i in l:
		res+=i
	
	print("和为{}".format(res))


if __name__ =='__main__':
	m,n = eval(input("输入两个整型数:"))
	adc(m,n)
