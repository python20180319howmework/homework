'''
创建3个任务进程,分别统计创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行
'''
from multiprocessing import Process

def mycount(n):
    m = []
    with open(n,'r') as f:
        while True:
            if f.readline() == '':
                break
            else:
                m.append(f.readline())
        print('{}有{}行文件'.format(n,len(m)))
               
if __name__ == '__main__':
    l = []
    for i in ["/etc/passwd","/etc/group","/etc/bashrc"]:
        p = Process(target=mycount,args=(i,))
        p.start()
        l.append(p)
    for i in l:
        i.join()
