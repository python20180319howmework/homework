'''
使用多进程模型实现,父进程将命令行所跟的文件发送给子进程,
子进程将收到的文件打印出来 python hw2.py “/etc/passwd”
'''

from multiprocessing import Process,Pipe
import time

def pro(out,inn):
    inn.close()
    while True:
        try:
            print(out.recv())
        except:
            out.close()
            break
if __name__ == '__main__':
    out_pipe,inn_pipe=Pipe()
#    out_pipe.close()
    p=Process(target=pro,args=(out_pipe,inn_pipe))
    p.start()
    out_pipe.close()
    f=open("/etc/passwd",'r')
    for i in f.readlines():
        inn_pipe.send(i)
        time.sleep(1)
    inn_pipe.close()
#    f.close()
    p.join()
