'''
创建3个任务进程,分别统计"/etc/passwd"
“/etc/group” “/etc/bashrc”文件有多少行
'''
from multiprocessing import Process
def myprint(flname):
    f=open(flname,'r')
    l=[]
    for i in f.readlines():
        l.append(i)
    print(len(l))

if __name__ == '__main__':
    for i in ['/etc/passwd','/etc/group','/etc/bashrc']:
        p=Process(target=myprint,args=(i,))
        p.start()
        p.join()

