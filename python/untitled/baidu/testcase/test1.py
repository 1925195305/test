#! /usr/bin/python
#-*- coding:utf-8 -*-
from src.func.func_1 import wx,wb,qq,mm
from appium import webdriver
from time import sleep
import unittest
from jiekou.cs.HTMLTestRunner import HTMLTestRunner
from src.until.qwe import REPORT_DIR
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        a={
          "platformName": "Android",
          "platfornVersion": "5.1.1",
          "deviceName": "emulator-5554",
          "appPackage": "com.baidu.input",
          "appActivity": ".ImeAppMainActivity"
        }
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
        sleep(10)
        # g.info('建立连接成功!')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
