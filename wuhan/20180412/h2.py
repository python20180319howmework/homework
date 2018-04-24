'''
升级w7实例,使得服务器可以同时响应多个客户端请求(建议多线程)
'''

from socket import  *
import time
import threading

SERVER_IP = "172.25.1.234"
SERVER_PORT = 1234
server_sd = socket(AF_INET, SOCK_STREAM)
server_sd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server_sd.bind((SERVER_IP, SERVER_PORT))
server_sd.listen(10)

def myServer(n,r):
        print("recive the new connect, the addr %s:%s", r)
        n.send(b'welcome connect me')
        rcvdata = n.recv(1024)
        print("recive data is %s" % rcvdata.decode('utf-8'))
        snddata = time.ctime() + rcvdata.decode('utf-8')
        n.send(snddata.encode('utf-8'))
        time.sleep(100)
        server_sd.close()

if __name__ == '__main__':
    while True:
        newsd, remote_addr = server_sd.accept()
        t = threading.Thread(target=myServer, args=(newsd, remote_addr))
        t.start()