#2.使用多进程模型实现,父进程将命令行所跟的文件发送给子进程,
# 子进程将收到的文件打印出来
# python hw2.py “/etc/passwd”
from multiprocessing import Pipe,Process
import sys   # sys.argv 命令行参数List，第一个元素是程序本身路径

def jobs(out,inn):
	inn.close()
	with open(out.recv(),'r') as f:
		while True:
			if f.readline() == '':
				break
			else:
				print(f.readline())
if __name__ == '__main__':
	out_pipe, in_pipe = Pipe()
	p = Process(target= jobs, args= (out_pipe,in_pipe))
	p.start()
	out_pipe.close()
	in_pipe.send(sys.argv[1])
	in_pipe.close()
	p.join()
