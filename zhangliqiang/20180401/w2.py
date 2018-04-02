


#2.用递归方式实现pow(x, y)的功能，你的函数名为mypow() 

def mypow(x, y):
	if y == 1:
		return x
	elif y > 1:
		return(x * mypow(x,(y-1)))
if __name__ == '__main__':	
	x,y = eval(input("请输入两个数字x,y"))
	print("{}的{}次幂为{}".format(x,y,mypow(x,y)))
