#5. 使用递归函数，实现求得斐波那契数列的第n项

def fibo(n):
		if n <= 1:
			return n
		else:
			return(fibo(n - 1)+ fibo(n - 2))
a = int(input("请问要输出第几项"))
if a <= 0:
	print("请输入正数")
else:
	for i in range(a):
		print(fibo(i))






























