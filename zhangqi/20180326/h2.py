
#输入一个三为整型数,判断是否是一个水仙花数
#计算出有多少各水仙花数

num = int (input("请输入一个三位整型数："))
a = num % 10
b = num // 10 % 10
c = num //100 % 10
if num == a**3 + b**3 + c**3:
	print ("%s 是水仙花数" % num)
else:
	print("%s 不是水仙花数" % num)
n = 0
for i in range (100,1000):
	a1 = i % 10
	b1 = i//10 % 10
	c1 = i //100 % 10
	if i == a1 ** 3 + b1 ** 3 + c1 ** 3:
		print(i)
		n = n + 1
	else:
		continue
print("共有%s 个水仙花数" % n)	

while num >= 0:
	a1 = num % 10
	sum1 += pow(a1, 2)
	num = num //10 
for i in range(100,1000):
	if sum1 == num:
		print("{}是水仙花数".format(num))
		n += 1
else:
	print("三位数总共有%s个水仙花数" % n)


















