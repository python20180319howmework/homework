def zs(num):
	if num > 1:
		for i in range(2,num):
			if num % i == 0:
				print("不是质数")
			break
		else:
			print("是质数")
	else:
   		print("不是质数")
if __name__=='__main__':
	a=int(input("请输入一个整数："))
	zs(a)
