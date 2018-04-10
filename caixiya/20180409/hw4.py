'''
4.现有两个进程,1号进程向文件写入10个"hello" 2号进程向文件写入10个"world",两个进程并发执行
如何使得文件中的内容一定是"hellohellohellohellohello.....worldworldworld......."
'''
from multiprocessing import Process,Lock

def func(name,arg,mylock):
    with mylock:
        f=open(name,"a")
        f.write(arg*10)
        f.close()

if __name__=='__main__':
    f=open("./caixiya.txt","w")
    f.close()
    mylock=Lock()
    p1=Process(target=func,args=("./caixiya.txt","hello",mylock))
    p1.start()
    p2=Process(target=func,args=("./caixiya.txt","world",mylock))
    p2.start()
    p1.join()
    p2.join()