n=int (input("please input a num:"))
if n==(n//100)*(n//100)*(n//100)+(n//10%10)*(n//10%10)*(n//10%10)\
+(n%100%10)*(n%100%10)*(n%100%10):
	print("{}是一个水仙花数".format(n))
else:
	print("{}不是一个水仙花数".format(n))
count=0
for i in range(100,1000):
	a=i%100%10
	b=i//10%10
	c=i//100
	if i==c*c*c+b*b*b+a*a*a:
		count=count+1
		print(i)
print("共有{}个水仙花数".format(count))
