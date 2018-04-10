'''
3.现有任务要去打印所有的三位数中的水仙花数,要求最多的任务进程不超过4个
'''
from multiprocessing import Pool

def shuixianhua(num):
    b=num//100
    s=num//10%10
    g=num%10
    if pow(b,3)+pow(s,3)+pow(g,3)==num:
        print("{}是水仙花数".format(num))

if __name__=="__main__":
    p=Pool(4)
    for i in range(100,1000):
        p.apply_async(shuixianhua,args=(i,))
    p.close()
    p.join()