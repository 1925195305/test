#! /usr/bin/python
#-*- coding:utf-8 -*-

# import requests
# import re
# # class qiushi():
# #     de
# a = 'https://www.qiushibaike.com/text/page/{}/'.format(1)
# #发送请求
# b=requests.get(a)
# #接受响应 1.text 文本读取方式(网页源代码)
# print(b.text)


# #
#
# #服务器(TCP)
# import socket  #套接字 是提供了通信双方最底层的功能
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个套接字，创建一个有接收能力和发送能力的对象 (默认使用TCP) UDP(SOCK_DGRAM)  AF_INET(ipv4协议)
# #绑定IP地址和端口
# s.bind(('192.168.1.18',51000)) #接收的是个元组
# s.listen(3) #监听服务有没有开启    最大等待个数
# while True:
#     #接收建立连接
#     client,addr=s.accept()  #第一个值是建立连接的信息，第二个值是客户端的ip地址和端口号
#     qwe=client.recv(1024) #接收客户端发送的请求  1024每次接收的最大字节
#     print(qwe.decode('utf-8'))
#     er=input('>>>>>>')
#     client.send(er.encode('utf-8'))#发送响应
#
#
# #服务器(UDP)
# import socket  #套接字 是提供了通信双方最底层的功能
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建一个套接字，创建一个有接收能力和发送能力的对象 (默认使用TCP) UDP(SOCK_DGRAM)  AF_INET(ipv4协议)
# #绑定IP地址和端口
# s.bind(('192.168.1.18',51000)) #接收的是个元组  不用监听
# while True:
#     # #接收建立连接
#     client,addr=s.recvfrom(1024)#第一个值是建立连接的信息，第二个值是客户端的ip地址和端口号
#     print(client.decode('utf-8'))
#     msg='好啊好啊'
#     s.sendto(msg.encode('utf-8'),addr)
#
#




# #客户端(TCP)
# import socket
# while True:
#     sock =socket.socket() #不需要绑定ip,建立连接
#     sock.connect(('192.168.1.18',51000)) #服务器的ip和端口号
#     msg=input('>>>>>>>')#发送请求
#     sock.send(msg.encode('utf-8'))
#     qwe=sock.recv(1024)
#     print(qwe.decode('utf-8'))
#     # sock.close()#断开连接


# # #客户端(UDP)
# import socket
# sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #不需要绑定ip,建立连接
# #不需要建立连接
# host= ('192.168.1.18',51000)
# msg='你好啊'
# sock.sendto(msg.encode('utf-8'),host)
# reg=sock.recv(1024)
# print(reg.decode('utf-8'))
# sock.close()
