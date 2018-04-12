from time import sleep, ctime
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
    getfibo(15)
    jiecheng(15)
    qianhe(15)
    print("结束啦", ctime())