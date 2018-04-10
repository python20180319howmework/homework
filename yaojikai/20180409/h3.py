'''
3.现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个
'''
from multiprocessing import Pool
import os


def myprocess(n):
    print("the process [%d] running" % os.getpid())
    for hua in range(100,1000):
        if hua == ((hua%10)*(hua%10)*(hua%10))+((hua//10%10)*(hua//10%10)*(hua//10%10))+((hua//100%10)*(hua//100%10)*(hua//100%10)):
            print("{}是水仙花数".format(hua))

if __name__ == '__main__':

    p = Pool(4)
    for i in range(4):
        p.apply_async(myprocess,args=(1,))
    p.close()
    p.join()