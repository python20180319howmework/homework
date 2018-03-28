
'''
定义一个函数，计算给定的整型数是否为质数
'''
def hanshu(m):
	for i in range(2,m):
		if m%i==0:
			print("不是质数")
			break
		else:
			print("是质数")
			break



if __name__=='__main__':
	a=int(input("请输入一个整数："))
	hanshu(a)
