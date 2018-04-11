#1.创建3个任务进程,
# 分别统计"/etc/passwd" “/etc/group” “/etc/bashrc”文件
# 有多少行
from multiprocessing import Process
import os

def job(arg):
	l = []
	f = open(arg,'r')
	for line in f.readlines():
		l.append(line)
	print(len(l))
if __name__ == '__main__':
	p1 = Process(target = job, args =("/etc/passwd",) )
	p2 = Process(target = job, args =("/etc/group",) )
	p3 = Process(target = job, args =("/etc/bashrc",) )

	for i in [p1,p2,p3]:
		i.start()
		i.join()
























