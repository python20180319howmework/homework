'''
创建3个任务进程,分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件有多少行
'''
from multiprocessing import Process

def newProcess(flname):
    f = open(flname,'r')
    count = len(f.readlines())
    print('{}有{}行'.format(flname,count))
    f.close()
if __name__ == '__main__':
    l = []
    for i in ['/etc/passwd','/etc/group','/etc/bashrc']:
        p = Process(target=newProcess,args=(i,))
        p.start()
        l.append(p)
    for i in l:
        i.join()

