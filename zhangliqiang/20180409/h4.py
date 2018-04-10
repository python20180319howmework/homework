#4.现有两个进程,1号进程向文件写入10个"hello" 2号进程向文件写入10个"world",两个进程并发执行
#如何使得文件中的内容一定是"hellohellohellohellohello.....worldworldworld......."

from multiprocessing import Process, Pool, Lock

import time, os


def newprocess(flname, mylock):
    mylock.acquire()
    time.sleep(1)


    f1 = open(flname, "r+")
    fistline = f1.readline()
    fistline = fistline + "hello"
    f1.seek(0, 0)
    f1.write(fistline)
    f1.close()
    mylock.release()
    mylock.acquire()
    time.sleep(0.1)
    f2 = open(flname, "r+")
    fistline = f2.readline()
    fistline = fistline + "world"
    f2.seek(0, 0)
    f2.write(fistline)
    f2.close()
    mylock.release()


if __name__ == '__main__':
    f1 = open("./myprocess.txt", "w")
    f1.write("")
    f1.close()

    mylock = Lock()

    pl1 = []
    for i in range(10):
        p1 = Process(target=newprocess, args=("./myprocess.txt", mylock))
        p1.start()
        pl1.append(p1)
    for l in pl1:
        l.join()
    f2 = open("./myprocess.txt", "w")
    f2.write("")
    f2.close()



    pl2 = []
    for i in range(10):
        p2 = Process(target=newprocess, args=("./myprocess.txt", mylock))
        p2.start()
        pl2.append(p2)
        for l in pl2:
            l.join()