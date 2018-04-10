'''
4.现有两个进程,1号进程向文件写入10个"hello" 2号进程向文件写入10个"world",两个进程并发执行
如何使得文件中的内容一定是"hellohellohellohellohello.....worldworldworld......."

'''
from multiprocessing import Process,Lock

def new1write(name,mylock):
    with mylock:
        f = open(name,'r+')
        f.write('hello'*10)
        f.close()

def new2write(name,mylock):
    with mylock:
        f = open(name,'r+')
        c = f.read()
        f.seek(0,0)
        f.write(c+'world'*10)
        f.close()

if __name__ == '__main__':
    f = open('./my.txt','w')
    f.close()
    mylock = Lock()
    p1 = Process(target=new1write,args=('./my.txt',mylock))
    p2 = Process(target=new2write,args=('./my.txt', mylock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()








