#! /usr/bin/python
#-*- coding:utf-8 -*-

import unittest
from jiekou.config.qingqiu import jiekou_qinqiu
from jiekou.data.duqu import shuju
class qwe(unittest.TestCase):
     bb=jiekou_qinqiu().denglu
     cc=shuju()
     def test_1(self):
         aa=self.bb(int(self.cc[0][0]),int(self.cc[0][1]))
         self.assertEqual(aa['code'],0)
     def test_2(self):
         for j in range(1,len(self.cc)):
           bb=self.bb(int(self.cc[j][0]),int(self.cc[j][1]))
           self.assertNotEqual(bb['code'],0)
# if __name__ == '__main__':
#     unittest.main()


