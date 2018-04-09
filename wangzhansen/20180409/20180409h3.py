'''
3.现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个
'''
from multiprocessing import Process, Pool

import os
def job(n):
    gewei = n % 10
    shiwei = (n // 10) % 10
    baiwei = (n // 100) % 10
    if shuru == (gewei ** 3) + (shiwei ** 3) + (baiwei ** 3):
        print("%d是水仙花数" % n)
    else:
        print("%d不是水仙花数" % n)

if __name__ == '__main__':
    p = Pool(4)
    for i in range(100,1000):
       p.apply_async(job, args=(i,))
    p.close()
    p.join()