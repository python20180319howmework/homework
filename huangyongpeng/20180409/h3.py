'''
现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个

'''
from multiprocessing import Process,Pool
def shuixian(arg):
    if arg==(arg%10)**3+(arg//10%10)**3+(arg//100)**3:
        print("{}是水仙花数".format(arg))
    else:
        pass
if __name__ == '__main__':
    p=Pool(4)
    for i in range(100,1000):
        p.apply_async(shuixian,args=(i,))
    p.close()
    p.join()