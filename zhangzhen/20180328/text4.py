'''
4. 定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
'''
a,b=eval(input("请输入两个整型数："))
def run(a,b):
	sum1 = 0
	for i in range(b):
		sum1 =  sum1+a*((b-i)*pow(10,i))
		i += 1
	return sum1
print(run(a,b))	

#定义一个列表
#分别把 3,33,333，'''添加到列表
#最后求列表的和
