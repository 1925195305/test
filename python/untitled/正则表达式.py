#! /usr/bin/python
#-*- coding:utf-8 -*-
#正则表达式
import  re
a='wqerw3f4233f24'
#compile() 编译，将[0-9]*编译成正则语言(正则条件)
p=re.compile('f(.*)f')
#findall 从某个地方查找所有符合正则的字符串,findall本身也有编译功能
# c=re.findall('[0-9]{2,4}',a)
#如果有两个参数：1，正则条件 2，查找范围
# c=re.findall(p(正则条件),a(查找范围))
#有一个参数时：1，查找范围
c=p.findall(a)


#findall的两种用法
# c=re.findall('[0-9]{2,4}',a)(正则.findall)
# c=p.findall(a)(条件.findall)
# print(c)

#########################################
# import  re
# a='wfqerw3f4233f24f'
# p=re.compile('f(.*)f') #只匹配指定内容给正则条件加括号
# c=p.findall(a)
# print(c)
############################################

#1贪婪模式  尽可能匹配跟多 的内容
# a = 'wfqerw3f4233f24f'
# p=re.compile('f(.*)f')
# print(p)
#2非贪婪模式  尽可能匹配少的内容，加问号
# p=re.compile('f(.*？)f')


# ##.(点)是可以匹配字符，除换行符之外
#re.S 给点加功能，可以匹配换行符在内的任意字符
# p=re.compile('f(.*？)f',re.S)
#re.I 给条件加能，不区分大小写
# p=re.compile('f(.*？)f',re.I)
