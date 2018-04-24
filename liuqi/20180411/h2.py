"""
作者：刘琪
时间：18-4-12
题目：升级w7实例,使得服务器可以同时响应多个客户端请求(建议多线程)
"""
from socket import *
import time

#
SERVER_IP = "172.25.0.134 "
SERVER_PORT = 12345

#
server_sd = socket(AF_INET, SOCK_STREAM)

server_sd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#
server_sd.bind((SERVER_IP, SERVER_PORT))

#
server_sd.listen(100)

while True:
    #
    newsd, remote_adds = server_sd.accept()
    print("recive the new connect, the addr %s:%s", remote_adds)

    # 向客户端发送消息
    while True:
        massage = input("请输入：")
        newsd.send(massage.encode("utf-8"))

        # 接收客户端消息
        rcvdata = newsd.recv(1024)
        print("%s" % rcvdata.decode("utf-8"))
    # senddata = time.ctime() + rcvdata.decode("utf-8")
    # newsd.send(senddata.encode("utf-8"))
    server_sd.close()

server_sd.close()