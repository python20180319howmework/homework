'''
2.使用多进程模型实现,父进程将命令行所跟的文件发送给子进程,子进程将收到的文件打印出来
    python hw2.py “/etc/passwd”
'''
from multiprocessing import Pipe, Process

def job(inn,out):
    inn.close()
    while True:
        try:
            print(out.recv())
        except:
            out.close()
            break

if __name__=='__main__':
    in_pipe,out_pipe=Pipe()
    p=Process(target=job,args=(in_pipe,out_pipe))
    p.start()
    out_pipe.close()
    f=open("/etc/passwd","r")
    for line in f.readlines():
        in_pipe.send(line)
    in_pipe.close()
    p.join()