#! /usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
# class DS(object):
d={
        "platformName": "Android",
        "platfornVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "com.baidu.input",
        "appActivity": ".ImeAppMainActivity"
}
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
sleep(10)
dr.find_element_by_id('com.baidu.input:id/banner_settings').click()
sleep(1)
a=dr.find_element_by_id('android:id/list').find_elements_by_class_name('android.widget.RelativeLayout')
print(a)
a[0].click()
dr.find_element_by_id('com.baidu.input:id/banner_settings').click()


# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15518117087')
# sleep(1)