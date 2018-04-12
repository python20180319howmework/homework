'''
2.升级w7实例,使得服务器可以同时响应多个客户端请求(建议多线程)
'''
from socket import *
import threading

SERVER_IP = "172.25.2.189"
SERVER_PORT = 33333

# 创建流式套接字对象
server_sd = socket(AF_INET, SOCK_STREAM)
#表明地址可以重复使用
server_sd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 将本地地址与套接字对象绑定  必须绑定,这样客户端才知道与谁链接
server_sd.bind((SERVER_IP,SERVER_PORT))
# 使得套接字处于监听状态, 参数指明最大的链接个数
server_sd.listen(100)

def sc(lock):
    lock.acquire()
    while True:
        # 等待接收客户端的请求
        newsd, remote_addr = server_sd.accept()  # newsd用于数据交换的套接字  remote_add 对端地址    print("recive the client connect, the addr %s:%s" % remote_addr)
        # 向客户端发送消息
        newsd.send(b'welcome connection me')
        # 接收客户端消息
        rcvdata = newsd.recv(1024)
        print("客户端给我回复了%s" % rcvdata.decode('utf-8'))
        snddata =input("please:")
        newsd.send(snddata.encode('utf-8')) # python3 str--->unicode  网络传输的数据bytes  unicode--->bytes (encode)
    lock.release()
if __name__ == '__main__':
    lock=threading.Lock()
    l=[]
    for i in range(10):
        t=threading.Thread(target=sc,args=(lock,))
        t.start()
        l.append(t)
    for i in l:
        i.join()
server_sd.close()
