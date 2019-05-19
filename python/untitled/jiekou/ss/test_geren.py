#! /usr/bin/python
#-*- coding:utf-8 -*-
import unittest
class asd(unittest.TestCase):
    def test_geren_chenggeng(self):
        self.assertNotEqual(['msg'],"OK")
    def test_geren_shibai(self):
        self.assertNotEqual(['code'],0)
