#1.创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行
from  multiprocessing import  Process
import  os
def job1(arg):

    f = open(arg,'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))

def job2(arg):
    f = open(arg,'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))
def job3(arg):
    f = open(arg, 'r')
    for line in f.readlines():
        l.append(line)
    print(len(l))
if __name__ == '__main__':
    l = []
    p1 = Process(target=job1, args=('/etc/passwd',))
    p1.start()
    p2 = Process(target=job2, args=('/etc/group',))
    p2.start()
    p3 = Process(target=job3, args=('/etc/bashrc',))
    p3.start()