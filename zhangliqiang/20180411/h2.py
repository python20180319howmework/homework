'''
作者:zlq
日期:18-4-11
'''
#2.升级w7实例,使得服务器可以同时响应多个客户端请求(建议多线程)

import socket
import threading
from time import sleep
def response(sock,addr):
    print ("收到请求")
    data = sock.recv(1024)
    print (data)
    sock.send(html)
    sock.close()
html = '''Hello world!'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1990))
s.listen(50)
print ("正在等待连接……")
while True:
    sleep(0.1)
    sock,addr = s.accept()
    t = threading.Thread(target=response, args=(sock,addr))
    t.start()