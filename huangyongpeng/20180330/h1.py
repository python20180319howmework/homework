'''
 1) 计算所有参数的和的基数倍(默认基数为base=3)
'''
def jishu(base=3,*number):
	res=0
	for i in number:
		res+=i
	k=res*base
	return k


if __name__=="__main__":
	
	print(jishu(3,5,6,7,8))
	
