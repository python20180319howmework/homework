'''
编写一个函数：
   1) 计算所有参数的和的基数倍(默认基数为base=3)
'''
def sumpow(*num,base=3):
	sumn=0
	for i in num:
		sumn+=i
	return sumn*base

if __name__=="__main__":
	l=[1,2,3]
	print(sumpow(*l))	
