#! /usr/bin/python
#-*- coding:utf-8 -*-
# 第一步导入appium模块中的wbdriver
from appium import webdriver
from time import sleep

# 面向对程
# 测试脚本与appium服务器进行连接的参数
d = {
    "platformName": "Android",
    "platfornVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity"
}

# 写死的http://127.0.0.1:4723/wd/hub
# 测试脚本是appium服务器与手机建立连接的过程
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
# 可能元素还没有加载出来，需要休眠
sleep(10)

# 元素是id，使用id进行定位
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
# 获取微信文字,元素的多级定位，先定位上一级，再定位下面的元素，没有id，找class属性
# test=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# test2=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# test3=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# test4=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# print(test)
# print(test2)
# print(test3)
# print(test4)
# 插入时间，休眠几秒
sleep(2.0)
# send_keys()输入的是一个字符串
# 什么时候可以用send_keys()
# 向手机输入数据的时候
# clickablee为true时
# enabled为true时
# focused为true
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(2.0)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15518117087')
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('lv13792846')
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(5.0)

# 退出app，包括后台进程
dr.quit()