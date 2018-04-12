'''
创建三个函数,非别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''
import threading
from time import time,sleep
l=[]
def feibo(n=15):
    a=0
    b=1
    print("开始时间：%s" %time())
    l.append(time())
    for i in range(n):
        a,b=b,a+b
    print("一阶段结束时间：%s"%time())
    print(b)

def jiecheng(n=15):
    res=1
    print("二阶段开始时间：%s"%time())
    for i in range(1,n+1):
        res*=i
    print(res)
    print('二阶段结束时间：%s'%time())
def he(n=15):
    res=1
    print('三阶段开始时间：%s'%time())
    for i in range(1,n+1):
        res+=i

    print("三阶段结束时间：%s"%time())
    print(res)
    l.append(time())
def shijian():
    return int(l[1])-int(l[0])

if __name__ == '__main__':

    feibo(15)
    jiecheng(15)
    he(15)
    print(shijian())
