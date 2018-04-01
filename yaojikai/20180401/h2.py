#2.用递归方式实现pow(x, y)的功能，你的函数名为mypow() 
def mypow(a,b):
	if b == 1:
		return a
	elif b>1:
		return a*mypow(a,(b-1))
	else:
		print("请输入正确的数值")


if __name__ =="__main__":
		a,b = eval(input("请输入a，b"))
		print("{}的{}次方是{}".format(a,b,mypow(a,b)))







