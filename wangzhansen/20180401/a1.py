'''
2.用递归方式实现pow(x, y)的功能，你的函数名为mypow() 
'''
def mypow(x,y):
	if y == 0:
		return 1
	elif y == 1:
		return x
	return x * mypow(x ,y - 1)

print(mypow(2,3))


























