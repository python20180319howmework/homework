'''
定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
'''
def func(num1,num2):
	sum1=0
	sum2=0
	for i in range(num2):
		sum1+=num1*pow(10,i)
		sum2+=sum1
	return sum2
num1,num2=eval(input("请输入两个整型数："))
print("计算结果是{}".format(func(num1,num2)))
