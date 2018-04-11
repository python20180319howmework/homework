#3.现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个

import math

import os
from multiprocessing import  Process,Pool

def job(i):


    a1 = i // 100 % 10
    a2 = i // 10 % 10
    a3 = i % 10
    if i == a1 ** 3 + a2 ** 3 + a3 ** 3:

        print("%d 是水仙花数" % i)
if __name__ == '__main__':
    pl = Pool(3)
    for i in range(100, 1000):

        pl.apply_async(job, args=(i,))


    pl.close()
    pl.join()
