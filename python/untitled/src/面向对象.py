#! /usr/bin/python
#-*- coding:utf-8 -*-
from appium import  webdriver
from time import sleep

class DS(object):
    d = {
        "platformName": "Android",
        "platfornVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity"
    }

    # 建立连接函数
    def __init__(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(5)
     # 检查那四个文字的函数/方法

        # 获取微信
        test =self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        test2=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        test3=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        test4=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text

        print(test,test2,test3,test4)
        return test,test2,test3,test4

    #  关闭app的函数
    def close_app(self):
         self.dr.quit()
if __name__=='__main__':
    # 创建一个DS类实例，赋值给变量go
    go=DS()
    # 调用DS类的方法
    go.check_text()
    go.close_app()
