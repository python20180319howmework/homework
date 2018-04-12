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