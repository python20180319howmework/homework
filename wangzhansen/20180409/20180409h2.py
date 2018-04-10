'''
2.使用多进程模型实现,父进程将命令行所跟的文件发送给子进程,子进程将收到的文件打印出来
    python hw2.py “/etc/passwd”
'''
from multiprocessing import Process, Pool, Lock

import  os
def 