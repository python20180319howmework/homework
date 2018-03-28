'''
4,定义一个函数，完成以下功能:
  1) 输入两个整型数,例如输入的是3, 5
  2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
'''


def sum1sum(a,b):
	n = 0
	for i in range(1,b+1):   #将a转换成字符串复制i个，再将a转换成整型进行运算
		n += int(str(a)*i)
	return n

a,b = eval(input("请输入两个整型数，例如（3，5）："))
print("结果为：{}".format(sum1sum(a,b)))
		





