'''
多线程
'''
import datetime
import threading
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
    t1=threading.Thread(target=fbnq,args=(15,))
    t1.start()
    t2=threading.Thread(target=jiecheng,args=(15,))
    t2.start()
    t3=threading.Thread(target=sumn,args=(15,))
    t3.start()
    print("斐波那契数列的第{}项是{}".format(15,fbnq(15)))
    print("{}的阶乘是{}".format(15, jiecheng(15)))
    print("前{}项的和是{}".format(15, sumn(15)))
    t1.join()
    t2.join()
    t3.join()
    end=datetime.datetime.now()
    print(end-start)