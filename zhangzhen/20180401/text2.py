
#2.用递归方式实现pow(x, y)的功能，你的函数名为mypow()

def mypow(x,y):
	res = 0
	if y == 0:
		res = 1
	else:
		res = x *mypow(x,y-1)
	return res
print(mypow(2,2))


































