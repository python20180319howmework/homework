'''
使用多进程模型实现,父进程将命令行所跟的文件发送给子进程,子进程将收到的文件打印出来
    python hw2.py “/etc/passwd”

'''
from multiprocessing import Process,Pipe
import sys
import os
def jieshou(out,inn):
    in_p.close()
    while True:
        try:
            print(out_p.recv())
        except:
            out_p.close()
            break



if __name__ == '__main__':
    out_p,in_p=Pipe()
    p=Process(target=jieshou,args=(out_p,in_p))
    p.start()
    out_p.close()
    f=open("/etc/passwd",'r')
    for line in f.readlines():
        in_p.send(line)
    in_p.close()
    p.join()