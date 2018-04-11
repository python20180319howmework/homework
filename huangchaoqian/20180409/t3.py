#现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个
from multiprocessing import Process,Pool
import math
def job(n):
    if pow(n%10,3)+pow(n//100,3)+pow(n//10%10,3)==n:
        print("%d 是水仙花数" % n)

if __name__ == '__main__':
    pl=Pool()
    for i in range(100,1000):
        pl.apply_async(job,args=(i,))
    pl.close()
    pl.join()
