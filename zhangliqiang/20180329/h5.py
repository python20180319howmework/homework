#5. 使用递归函数，实现求得斐波那契数列的第n项

def fibo(n):
	if n<= 1:
		return n
	else:
		return(fibo(n-1)+fibo(n-2))

ms = int(input("输出哪项"))

if ms <= 0:
	print("错误")
else:
	print("斐波那契数列")
	for i in range(ms):
		print(fibo(i))
