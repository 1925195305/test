#! /usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()# 定义要打开的浏览器
dr.get('https://mail.qq.com')
sleep(2)
dr.switch_to.frame('login_frame')
sleep(1)
dr.find_element_by_id('img_out_1925195305').click()
sleep(2)
dr.switch_to_default_content()
sleep(1)
dr.find_element_by_xpath('//*[@id="composebtn"]').click()
sleep(2)
dr.switch_to_default_content()
sleep(1)
# dr.find_element_by_xpath('//*[@id="toAreaCtrl"]').send_keys('15518117087@163.com')
# sleep(2)
dr.switch_to.frame(dr.find_element_by_id('mainFrame'))
dr.find_element_by_xpath('//*[@id="toAreaCtrl"]').send_keys('15518117087@163.com')