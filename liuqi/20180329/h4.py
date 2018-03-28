"""
4. 定义一个函数，完成以下功能:
   1) 输入两个整型数,例如输入的是3, 5
   2) 此函数要计算的是3 + 33 + 333 + 3333 + 33333(到5个为止)
"""
num1 = input("请输入整型数num1：")
num2 = input("请输入整型数num2：")
def	mysum(num1,num2):
	yousum = 0
	for i in range(1,int(num2)+1):
		yousum += int(num1*i)
	return yousum
yousum = mysum(num1,num2)
print(yousum)

