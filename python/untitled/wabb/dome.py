#! /usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()# 定义要打开的浏览器
# dr.get('http://www.baidu.com')# 请求网页
# sleep(2)
# dr.get('file:///C:/Users/gzy/Desktop/abc.html')
# sleep(2)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
#
# ww = dr.switch_to_alert()# 将控制器切换到弹出框
#
# print(ww.text)# 获取弹出框上的文本

# ww.accept()# 点击确定
#
# ww.dismiss()# 点击取消
#
# ww.send_keys('babsb')# 输入数据
#
# ww.accept()# 点击确定


# dr.get('https://www.douban.com/')
# sleep(2)
#
# # print(dr.current_window_handle)# 获取当前的窗口标识
#
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# sleep(3)
# ww=dr.window_handles# 获取所有的窗口标识
# print(ww)
# 切换窗口
# 按照窗口打开顺序给窗口标号——唯一标识这个窗口的字符串
# dr.switch_to_window(ww[0])
#




