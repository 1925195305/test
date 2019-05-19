#! /usr/bin/python
#-*- coding:utf-8 -*-


import pymysql
# conn=pymysql.connect(
#     host="192.168.1.12",  # 数据库主机地址
#     port=3306,
#     user="root",  # 数据库用户名
#     passwd="123456") # 数据库密码
#
# (创建游标   类似于vim光标
# aa=conn.cursor()#)
# 执行sql语句
# aa.execute('create database py;')
# aa.execute('create table pyb(name char(255), age int,xb char(255), cj int);')
# aa.execute('select * from pyb;')
# aa.execute('show tables;')
# for i in range(100):
#   aa.execute('insert into pyb values("{}",{},"{}",{});'.format(123,12,12,123))
#   conn.commit()
# aa.execute('select * from pyb;')
# a=aa.fetchmany(3)
#  a=aa.fetchall()
# a=aa.fetchone()


# aa.execute('use py_test;')
# #fetchall () 获取上一个sql语句的结果   想要获取多个就在每个sql语句后面加 fatchall
#fetchmany() 获取上一个sql语句的结果  默认只获取结果中的第一个数据 括号里面传入数字写几就获取几个
#fetchone() 每次只获取一条结果
# conn.close() 断开连接
#conn.commit() 提交 (更新，删除，添加)
# a=aa.fetchall()
# print(a)


import pymysql
conn=pymysql.connect(
    host="192.168.1.6",
    port=3306,
    user="root",
    passwd="123456")
# while True:
aa=conn.cursor()
ss=aa.execute(input('查看数据库：'))
a = aa.fetchall()
print(a)
# cc=aa.execute( input('切换数据库：'))
# f = aa.fetchall()
# print(f)
