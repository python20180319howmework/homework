from socket import *
import time
import threading
addip='172.25.1.21'
addpo=1853
ser_sd=socket(AF_INET,SOCK_STREAM)
ser_sd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ser_sd.bind((addip,addpo))
ser_sd.listen(10)
def hf(lo):
    lo.acquire()
    while True:
        newsd,remote_addr=ser_sd.accept()
        print('收到的地址：%s:%s', remote_addr)
        newsd.send('欢迎你'.encode())
        rcvdata=newsd.recv(1024)
        print("收到信息：%s"%rcvdata.decode('utf-8'))
        snddata=time.ctime()+rcvdata.decode('utf-8')
        newsd.send(snddata.encode('utf-8'))
    lo.release()
if __name__ == '__main__':
    lo=threading.Lock()
    for i in range(10):
        t=threading.Thread(target=hf,args=(lo,))
        t.start()
    t.join()
    ser_sd.close()



