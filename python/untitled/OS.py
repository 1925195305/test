#! /usr/bin/python
#-*- coding:utf-8 -*-

import os
# os.remove()                  删除文件

# b= os.popen('ipconfig/all')
# # print(b.read())            ping

#print(os.getcwd())            获取当前所在的位置

# os.chdir(r'D:')
# print(os.getcwd())             切换目录


# print(os.listdir(''))   获取当前文件夹下面的文件 一个点代表当前目录
# a=os.listdir('.')

# a=os.path.split(r'‪C:\Users\gzy\Desktop\脚本.docx') 将文件与路径分隔开
# print(a)

# a=os.path.splitext(r'‪C:\Users\gzy\Desktop\脚本.docx') 将文件与后缀名分割开
# print(a)

# a=os.path.isdir('yy') #判断文件是否是个目录
# print(a)

# b=os.path.isfile('a.txt') #判断文件是否是普通文件
# # print(b)

# os.mkdir('aaa') #创建文件夹
# os.rmdir('aaa') #删除文件夹
#
# os.makedirs('bb/cc/dd')#创建递归文件夹
# os.removedirs('bb/cc/dd')#删除递归文件夹



import paramiko
# # ssh123=paramiko.SSHClient() #创建一个远程客户端
# # ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy) #跳过验证，不到know_hosts文件中查找
# # ssh123.connect(hostname='192.168.2.232',port=22,username='root',password='123456') #连接主机
# # stuin,stuout,stuerr=ssh123.exec_command('ls -l')
# # # stuin 执行的命令
# # # stuout 执行的结果
# # # stuerr 执行的报错
# # print(stuout.read().decode())
# # ssh123.close()
#
# ssh123=paramiko.Transport('192.168.2.232',22)# 建立一个通道
# ssh123.connect(username='root',password='123456')#
# sftp=paramiko.SFTPClient(ssh123) #创建一个sftp客户端
#
#         #要下载的文件    储存的本地位置
# sftp.get('install.log','./aaa') #从linux下载文件到Windows
#
# sftp.put(r'通讯.py','/home/dey1.py') #从Windows上传文件到linux


import smtplib               #封装了smtp协议
import email.mime.multipart #处理邮件中的组成部分
import email.mime.text     #处理邮件中的正文
while True:
    fj='1925195305@qq.com'   #定义一个发件人
    sj='1625190489@qq.com'     #定义一个收件人
    server='smtp.qq.com'      #定义一个服务器  根据发件人定 Ps：smtp.163.com
    passwd='fufnzpnwicilbcia'        #授权码  授予登录客户端的权限密码 ps:在网页里登录163邮箱，点设置pop3
    message=email.mime.multipart.MIMEMultipart() #创建一个空邮件
    message['From'] =fj     #添加一个发件人
    message['To']=sj        #添加一个收件人
    message['Subject']='你是猪吗？'  #添加一个主题
    text='哈哈哈\n  你是猪吗\n 你是猪吗\n  哈哈哈'     # 写邮件正文
    txt=email.mime.text.MIMEText(text) #处理正文文本
    message.attach((txt))
    # 添加附件
    att2 = email.mime.text.MIMEText(open('haha.JPG', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="haha.JPG"'
    ## 头部字段
    message.attach(att2)
    smtp123=smtplib.SMTP_SSL(server,465) #定义服务器

    smtp123.login(fj,passwd)#登录服务器

    smtp123.sendmail(fj,sj,message.as_string())#发送邮件
    print(1)
    # smtp123.close() #断开连接