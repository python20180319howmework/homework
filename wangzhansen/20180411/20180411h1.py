'''
1.创建三个函数,分别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''

from time import sleep,ctime
import  threading
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

def getfibo(n):
    sleep(2)
    print(fibo(n), ctime())


def jiecheng(n):
    if n == 0 or n == 1:
        return 1
    tal = 1
    for i in range(2, n + 1):
        tal *= i
    sleep(2)
    print(tal, ctime())

def qianhe(n):
    if n == 0 or n == 1:
        return 1
    he = 1
    for i in range(2, n + 1):
        he += i
    sleep(2)
    print(he, ctime())

#def main()t


if __name__ == '__main__':
    print("开始啦", ctime())
    t= threading.Thread(target=getfibo, args=(15,))
    t1 = threading.Thread(target=jiecheng, args=(15,))
    t2 = threading.Thread(target=qianhe, args=(15,))
    t.start()
    t1.start()
    t2.start()
    t.join()
    t1.join()
    t2.join()
    print("结束啦", ctime())