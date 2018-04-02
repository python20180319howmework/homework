#用递归方式实现pow(x, y)的功能，你的函数名为mypow() 
def mypow(x,n):		
	
	if n==0:
		if x!=0:
			return 1
		else:
			return "error"
	elif n>0:
		return mypow(x,n-1)*x
	
	else:
		return mypow(x,n+1)*(1/x)

if __name__=="__main__":
	x,y=eval(input("please input x,y:"))
	print(mypow(x,y))





