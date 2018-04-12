'''
现有两个进程,1号进程向文件写入10个"hello" 2号进程向文件
写入10个"world",两个进程并发执行 如何使得文件中的内容一定
是"hellohellohellohellohello.....worldworldworld......."
'''
from multiprocessing import Process,Lock
import  time
def job(flname,arg,mylock):
    with mylock:
       # time.sleep(10)
        f=open(flname,'a+')
        f.write(arg*10)
        f.close()

if __name__ == '__main__':
    f=open('./myprocess.txt','w')
    f.close()
    mylock=Lock()
    p1=Process(target=job,args=('./myprocess.txt','hello',mylock))
    p2=Process(target=job,args=('./myprocess.txt','world',mylock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
