#! /usr/bin/python
#-*- coding:utf-8 -*-
from src.testcase import HTMLTestRunner
import unittest

# from jiekou.ss.test_denglu import qwe

def Baogao(name):
    suit = unittest.TestSuite()
    # dis = unittest.defaultTestLoader.discover(r'C:\Users\gzy\Desktop\untitled\jiekou\ss',
    #                                           pattern='test_*.py')
    # for i in dis:
    #     suit.addTest(i)


    # for i in name:
    #
    #     dis =unittest.defaultTestLoader.discover(r'C:\Users\gzy\Desktop\untitled\jiekou\ss',pattern='test_{}.py'.format(i.strip()))
    #     for o in dis:
    #         suit.addTest(o)
    # f = open( 'ABC.html', 'wb')
    for i in name:
        dis = unittest.defaultTestLoader.discover(r'C:\Users\gzy\Desktop\untitled\jiekou\ss',
                                                  pattern='test_{}.py'.format(i.strip()))
        for j in dis:
            suit.addTest(j)
    f = open(r'C:\Users\gzy\Desktop\untitled\jiekou\cs\a.html', 'wb')

    # suit.addTest(qwe('test_1'))
    # suit.addTest(qwe('test_2'))
    # suit.addTest(unittest.makeSuite(qwe))
    # dis=unittest.defaultTestLoader.discover(r'‪C:\Users\gzy\Desktop\untitled\jiekou\ss',pattern='test_{}.py'.format(i.strip()))
    # for i in dis:
    #     suit.addTest(i)
    # f = open('cc.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='巩紫阳', description='结果如下')
    runner.run(suit)
    f.close()
# Baogao()
if __name__=='__mian__':
   pass