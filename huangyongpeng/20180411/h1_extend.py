import threading
from time import time,sleep

def feibo(n=15):
    a=0
    b=1
    print("开始时间：%s" %time())

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
if __name__ == '__main__':


    t=threading.Thread(target=feibo,args=())
    t1=threading.Thread(target=jiecheng,args=())
    t2=threading.Thread(target=he,args=())
    t.start()
    t1.start()
    t2.start()
    t.join()
    t1.join()
    t2.join()