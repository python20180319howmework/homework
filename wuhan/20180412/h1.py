'''
创建三个函数,非别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''

from time import *
import threading

def fib_re(n):
    if n < 1:
        print("Wrong input! ")
        return -1
    else:
        if(n == 1 or n == 2):
            return 1
        else:
            return fib_re(n-1) + fib_re(n-2)

def muls(n):
    factorial = 1
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        return factorial

def adds(n):
    factorial = 1
    if n <= 0:
        return -1
    else:
        for i in range(1, n + 1):
            factorial = factorial + i
        return factorial - 1

if __name__ =='__main__':
    print(fib_re(15))
    print(muls(15))
    print(adds(15))
    print('单线程开始时间{}'.format(time()))
    fib_re(15)
    muls(15)
    adds(15)
    print('单线程结束时间{}'.format(time()))

    print('多线程开始时间{}'.format(time()))
    l = []
    for i in [fib_re, muls, adds]:
        t = threading.Thread(target=i, args=(15,))
        l.append(t)
    for i in range(len(l)):
        l[i].start()
    for i in range(len(l)):
        l[i].join()
    print('多线程结束时间{}'.format(time()))
