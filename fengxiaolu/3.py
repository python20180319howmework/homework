shu=int(input("输入一个三位整型数"))
a=shu%10
b=shu//10%10
c=shu//100
num=0
if shu == a*a*a+b*b*b+c*c*c:
	print("{}是水仙花数".format(shu))
else:
	print("{}不是水仙花数".format(shu))


for shuzi in range(111,1000):
	d=shuzi%10
	e=shuzi//10%10
	f=shuzi//100
	if shuzi == d*d*d+e*e*e+f*f*f:
		num=num+1
		print("{}是水仙花数".format(shuzi))
print("有{}个水仙花数".format(num))







