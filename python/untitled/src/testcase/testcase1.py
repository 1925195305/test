#! /usr/bin/python
#-*- coding:utf-8 -*-
# 导入函数
from src.func.func_1 import wx,wb,qq,mm
from appium import webdriver
from time import sleep
import unittest
from jiekou.cs.HTMLTestRunner import HTMLTestRunner
from src.until.qwe import REPORT_DIR
from src.testcase.a import get_logger
# 给日志一个变量g，g是全局变量
g=get_logger(name='testcase1.py')
# 测试脚本
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 建立连接
        a = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity"
        }
        # app建立连接
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
        sleep(10)
        g.info('建立连接成功!')
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        g.info('app关闭')
    #测试用例的代码
    def test_wx(self):
 #        验证微信的用例
        g.info('执行用例')
        text=wx(self.dr)
 #        断言
        self.assertEqual(text,'微信')
# 也可以 self.assertEqual(text(self.dr),'微信')

    def test_wb(self):
        g.info('执行用例')
        #        验证微博的用例
        text = wb(self.dr)
        #        断言
        self.assertEqual(text, '微博')

    def test_qq(self):
        g.info('执行用例')
        #        验证qq的用例
        text = qq(self.dr)
        #        断言
        self.assertEqual(text, 'QQ')

    def test_mm(self):
        g.info('执行用例')
        #        验证密码的用例
        text = mm(self.dr)
        #        断言
        self.assertEqual(text, '密码')

 #      运行测试脚本
if __name__=='__main__':
#    创建测试套件
 suite=unittest.TestSuite()
# 向测试套件中添加测试用例
 suite.addTest(Test('test_wx'))
 suite.addTest(Test('test_wb'))
 suite.addTest(Test('test_qq'))
 suite.addTest(Test('test_mm'))
 # 将测试结果写入html文件中
 # 生成测试报告路径
 # 将路径写活
 lu_jin=REPORT_DIR+r'C:\Users\gzy\Desktop\untitled\src\report'
 f = open(lu_jin, 'wb')
 runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='巩紫阳', description='结果如下')
 runner.run(suite)
