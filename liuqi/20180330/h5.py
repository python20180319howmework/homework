"""
使用递归函数，实现求得斐波那契数列的第n项
"""
def recur_fibo(n):
   
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
 
# 获取用户输入
nterms = int(input("您要输出几项 "))
 
# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(recur_fibo(i))
