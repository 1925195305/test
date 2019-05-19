#! /usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest
class DS(unittest.TestCase):
    d = {
        "platformName": "Android",
        "platfornVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity"
    }

    # 建立连接函数
    # def setUp(self):
    #     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
    #     sleep(5)
    #固定写法
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
        sleep(5)
        # 检查那四个文字的函数/方法
    def test_1(self):
        # 获取微信
        text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        # print(text)
        self.assertEqual(text,'微信')
    def test_2(self):
        text2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text2, '微博')
    def test_3(self):
        text3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text3, 'QQ')
    def test_4(self):
        text4 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
        self.assertEqual(text4, '密码')
    # def test_1(self):


    @classmethod
    def tearDownClass(cls):
            sleep(2.0)
            cls.dr.quit()

        # print(text)
        # return text

    #  关闭app的函数


if __name__ == '__main__':
    unittest.main()
    # # 创建一个DS类实例，赋值给变量go
    # go = DS()
    # # 调用DS类的方法
    # go.check_text()
    # go.close_app()

