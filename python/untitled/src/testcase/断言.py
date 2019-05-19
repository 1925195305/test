#! /usr/bin/python
#-*- coding:utf-8 -*-
# from time import sleep
# import unittest
# from appium import webdriver
# class ce(unittest.TestCase):
#  a = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.qk.butterfly",
#     "appActivity": ".main.LauncherActivity"
# }
#  @classmethod
#  def setUpClass(cls):
#   cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
#  def join(self,name,password):
#         sleep(2)
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#         sleep(2)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
#         sleep(2)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#         sleep(2)
#         print('准备登陆')
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(2)
#  def test_1(self):
#         self.join('15103819460','13137246872zls')
#         sleep(2)
#         print('开始断言')
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
#         self.assertEqual(text,'热门')
#  def logout(self):
#      a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
#      print(a)
#      a[3].click()
#      # 获取当前屏幕的分辨率 模拟手机上划
#      size = dr.get_window_size()
#      x1 = size['width'] * 0.5  # x坐标 50
#      y1 = size['height'] * 0.25  # 起始y坐标 50
#      y2 = size['height'] * 0.75  # 150
#      for i in range(2):
#          dr.swipe(x1, y2, x1, y1)
#      dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
#      sleep(1)
#      dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
#      sleep(1)
#      dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
#      sleep(1)
#      dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#      sleep(1)
#      dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
#      sleep(1)
#
#      @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
# if __name__ == '__main__':
#     unittest.main()

from time import sleep
import unittest
from appium import webdriver
# class ce(unittest.TestCase):
a = {
              "platformName": "Android",
              "platformVersion": "5.1.1",
              "deviceName": "emulator-5554",
              "appPackage": "com.qk.butterfly",
              "appActivity": ".main.LauncherActivity"
        }
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(2)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(1)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15518117087')
sleep(1)
# 清空
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
# sleep(1)·

dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('lv13792846')
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(2)
a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
print(a)
a[3].click()
# 获取当前屏幕的分辨率 模拟手机上划
size = dr.get_window_size()
x1 = size['width'] * 0.5  # x坐标 50
y1 = size['height'] * 0.25  # 起始y坐标 50
y2 = size['height'] * 0.75  # 150
for i in range(2):
    dr.swipe(x1, y2, x1, y1)
dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
sleep(1)
dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
sleep(1)
dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
sleep(1)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(1)
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
sleep(1)


#
#
