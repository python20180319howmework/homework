"""
5、使用递归函数，实现求得斐波那契数列的第n项

斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........

这个数列从第3项开始，每一项都等于前两项之和。
"""
def recur_fibo(n):
   
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
 
if __name__== "__main__":
# 获取用户输入
	nterms = int(input("您要输出几项 "))
 
# 检查输入的数字是否正确
	if nterms <= 0:
		print("输入正数")
	else:
		print("斐波那契数列:")
	for i in range(nterms):
		print(recur_fibo(i))
