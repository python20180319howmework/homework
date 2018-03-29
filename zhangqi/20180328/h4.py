#4. 定义一个函数，完成以下功能:
#   1) 输入两个整型数,例如输入的是3, 5
#   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)

def sum1(m, n):
	sumnum = 0
	for i in range(1,n+1):
		sumnum = sumnum + int(str(m)*i)
	return sumnum		
	print("结果是{}".format(sumnum))
a, b = eval(input("请输入两个整型数"))
print(sum1(a, b))















