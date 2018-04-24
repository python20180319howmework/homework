"""
作者：刘琪
时间：2018-4-11
题目：
    1.创建三个函数,分别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
    请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
    假定n的值是15

"""
import _thread
import time
from datetime import datetime

def Fibonacci_1(n):
    if n < 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        fnum = Fibonacci_1(n-1)+Fibonacci_1(n-2)
        return fnum
def Fibonacci_2(n):
    #print("Ｆ２开始时间:", time.ctime())
    if n == 0:
        return 1
    else:
        return n*Fibonacci_2(n-1)
    #print("Ｆ２结束时间:", time.ctime())


def Fibonacci_3(n):
    #print("Ｆ３开始时间:", time.ctime())
    num_3 = 0
    for i in range(0,n+1):
        num_3 += i

    return num_3
    #print("Ｆ３结束时间:", time.ctime())


def main_1():
    start = round(time.time() * 1000)
    start_ = datetime.utcnow()
    #print("开始时间是：%s",time.ctime())
    print(Fibonacci_1(15))
    print(Fibonacci_2(15))
    print(Fibonacci_3(15))
    #print("结束时间是：%s",time.ctime())
    end = round(time.time() * 1000)
    end_ = datetime.utcnow()
    print("单线程用时:", end_ - start_)
def main_2():
    #print("多线程开始时间:", time.ctime())
    start = round(time.time()*1000)
    start_ = datetime.utcnow()
    _thread.start_new_thread(Fibonacci_1, (15,))
    _thread.start_new_thread(Fibonacci_2, (15,))
    _thread.start_new_thread(Fibonacci_3, (15,))
    #print("多线程结束时间:",time.ctime())
    end = round(time.time() * 1000)
    end_ = datetime.utcnow()
    print("多线程用时:", end_ - start_)

if __name__ == '__main__':
    main_1()
    main_2()



