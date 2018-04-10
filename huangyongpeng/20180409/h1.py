'''
创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行

'''
from multiprocessing import Process
def first1(arg):
    f=open(arg,'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))
def second(arg):
    f=open(arg,'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))
def third(arg):
    f=open(arg,'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))
if __name__ == '__main__':
    l=[]
    p1=Process(target=first1,args=('/etc/passwd',))
    p1.start()
    p2=Process(target=second,args=('/etc/group',))
    p2.start()
    p3 = Process(target=third, args=('/etc/bashrc',))
    p3.start()