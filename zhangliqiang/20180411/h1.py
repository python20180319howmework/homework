'''
作者:zlq
日期:18-4-11

1.创建三个函数,非别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''

import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):  # 传参数
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())










def fibo(n1):
    sleep(0.005)
    if n1<= 1:
        return n1
    else:
        return(fibo(n1-1)+fibo(n1-2))
f = fibo(15)
print(f,ctime())

def factorial(x):
    sleep(0.1)
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
s = factorial(15)
print(s,ctime())
    # 前m项
def febn(m1):
    sleep(0.1)

    result1 = 0
    for i1 in range(1, m1 + 1):
            result1 += i1
    return result1

g = febn(15)
print(g,ctime())
funcs = (fibo,factorial,febn)

n = 15
def main():
    nfuncs = range(len(funcs))

    print('*** start ***')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('\n*** END ***')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
    print(threads[i].getResult())

    print('--all over at:', ctime())
if __name__ == '__main__':
    main()


