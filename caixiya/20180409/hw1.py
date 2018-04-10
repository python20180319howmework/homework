'''
1.创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行
'''
from multiprocessing import Process

def count(name):
    f=open(name,"r")
    for line in f.readlines():
        l.append(line)
    print(len(l))
    f.close()

if __name__=='__main__':
    l=[]
    p1=Process(target=count,args=("/etc/passwd",))
    p1.start()
    p1.join()
    p2=Process(target=count, args=("/etc/group",))
    p2.start()
    p2.join()
    p3=Process(target=count, args=("/etc/bashrc",))
    p3.start()
    p3.join()