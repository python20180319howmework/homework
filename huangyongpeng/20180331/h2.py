'''
用递归方式实现pow(x, y)的功能，你的函数名为mypow() 



'''
def  mypow(m,n):		
	if n==0:
		return 1
	else:
		return m*mypow(m,n-1)
if __name__=="__main__":
	a,b=eval(input("请输入俩数字："))
	print(mypow(a,b))
	
