#! /usr/bin/python
#-*- coding:utf-8 -*-

from jiekou.cs.baogao import Baogao
with open('a.txt','r') as f:
    bb = f.readlines()

if 'all' in bb:
    Baogao('*')
else:

    Baogao(bb)