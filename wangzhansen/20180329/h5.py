'''
5. 使用递归函数，实现求得斐波那契数列的第n项
'''
def fibo(n):
    x, y = 0, 1

    while(n):
        x,y,n = y, x+y, n - 1
    return x































