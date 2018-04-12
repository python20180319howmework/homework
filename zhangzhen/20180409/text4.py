#4.现有两个进程,1号进程向文件写入10个"hello"
# 2号进程向文件写入10个"world",两个进程并发执行
#如何使得文件中的内容一定是
# "hellohellohellohellohello.....worldworldworld......."

from multiprocessing import Process,Lock,Pool

def jobs(arg):
    with mylock:
        f = open('./zz.txt','a')
        f.write(arg*10)
        f.close()

if __name__ =='__main__':
    f = open('./zz.txt','w')
    mylock = Lock()
    p1 = Process(target=jobs,args=('world',))
    p2 = Process(target=jobs,args=('hello',))
    p1.start()
    p2.start()
    f.close()
    p1.join()
    p2.join()




















