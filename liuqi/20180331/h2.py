"""
2.用递归方式实现pow(x, y)的功能，你的函数名为mypow() 
"""

def mypow(x,y):
	
	if y:
		return x * mypow(x,y-1)
	else:
		return 1

if __name__ == "__main__":
	num1,num2 = eval(input("请输入两个整型数："))
	mynum = mypow(num1,num2)
	print("{}的{}次方结果是：{}".format(num1,num2,mynum))
	
