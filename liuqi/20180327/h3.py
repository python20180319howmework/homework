"""
3. 输入一个三位整型数，判断它是否是一个水仙花数
   (比如153 = 1*1*1 + 5*5*5 + 3*3*3)
   计算出有多少个水仙花数
"""
number = int(input("请输入一个三位整型数："))
num1 = (number % 10)**3
num2 = (number // 10 % 10)**3
num3 = (number // 100 % 10)**3
mysum = num1 + num2 + num3
num = 0
if mysum == number :
	print("输入的{}为水仙花数。".format(number))
else:
	print("输入的{}不是水仙花数。".format(number))
print("---------------------------------------------------------")
for i in range(100,1000):
	i_1 = (i%10)**3
	i_2 = (i//10%10)**3
	i_3 = (i//100%10)**3
	if i_1 + i_2 +i_3 == i:
		num += 1
else:
	print("三位数中水仙花数共有{}个".format(num))	
	 

