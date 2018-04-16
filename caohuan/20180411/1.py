'''
1.创建三个函数,分别的功能是, 求得斐波那契数列的第n项, 求n的阶乘,求n的前n项和
请比较三个函数单线程分别调用,和三个函数多线程并发的效率(相差多长时间)
假定n的值是15
'''
import datetime

def fbnq(n):
    summ=0
    if n==0:
        summ=0
    elif n==1:
        summ=1
    elif n>=2:
        summ=summ+fbnq(n-1)+fbnq(n-2)
    return summ

def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)

def sumn(n):
    summ=0
    for i in range(0,n+1):
        summ+=i
    return summ

if __name__=="__main__":
    start=datetime.datetime.now()
    print("斐波那契数列的第{}项是{}".format(15,fbnq(15)))
    print("{}的阶乘是{}".format(15, jiecheng(15)))
    print("前{}项的和是{}".format(15, sumn(15)))
    end=datetime.datetime.now()
    print(end-start)