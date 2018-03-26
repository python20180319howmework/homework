#3
hua = int(input("请输入一个三位整型数："))
a = hua%10
b = hua//10%10
c = hua//100%10
num=0
if hua == a*a*a+b*b*b+c*c*c:
	print("{}是水仙花数".format(hua))
else:
	print("{}不是水仙花数".format(hua),"\n")

for hua1 in range(111,1000):
	d = hua1%10
	e = hua1//10%10
	f = hua1//100%10
	if hua1 == d*d*d+e*e*e+f*f*f:
		num+=1
		print("三位数里{}是水仙花数".format(hua1))
print("共有{}个水仙花数".format(num))
		





