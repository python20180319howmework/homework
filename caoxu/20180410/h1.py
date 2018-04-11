'''
创建三个函数,非别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''
from time import *
import threading

def febncii(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return febncii(n-1)+febncii(n-2)

def factor(n):
    if n == 1:
        return 1
    else:
        return n*factor(n-1)

def num(n):
    return n*(1+n)/2

if __name__ == '__main__':
    print('斐波那契数列第15项为{}'.format(febncii(15)))
    print('15的阶乘为{}'.format(factor(15)))
    print('15的前n项和为{}'.format(num(15)))
    print('单线程开始时间{}'.format(time()))
    febncii(15)
    factor(15)
    num(15)
    print('单线程结束时间{}'.format(time()))

    print('多线程开始时间{}'.format(time()))
    l = []
    for i in [febncii,factor,num]:
        t = threading.Thread(target=i,args=(15,))
        l.append(t)
    for i in range(len(l)):
        l[i].start()
    for i in range(len(l)):
       l[i].join()

    print('多线程结束时间{}'.format(time()))