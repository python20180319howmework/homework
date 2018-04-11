'''
4.现有两个进程,1号进程向文件写入10个"hello" 2号进程向文件写入10个"world",两个进程并发执行
如何使得文件中的内容一定是"hellohellohellohellohello.....worldworldworld......."
'''
from multiprocessing import Process, Pool, Lock

import os
def newprocess(flname, mylock):
    with mylock:
        f = open(flname,"r+")
        fistline = f.readline()
        fistline = str("hello" * 10)
        f.seek(0,0)
        f.write(fistline)
        f.close()

if __name__ == '__main__':
    f = open("./yourprocess.txt", "w")
    f.write(",")
    f.close()
    mylock = Lock()
    p = Process (target= newprocess, args= ("./yourprocess.txt", mylock))
    p.start()
    q = Process (target= newprocess, args= ("./yourprocess.txt", mylock))
    q.start()