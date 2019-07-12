#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/25 15:10
# @Author  : Nana Xing
# @Site    : 
# @File    : client_demo.py
# @Software: PyCharm
import socket
import sys  # for exit

try:
    # 创建一个socket AF_INET指的是IPv4协议，AF_INET6指的是IPv6
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    sys.exit()

# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    f.write(html)
