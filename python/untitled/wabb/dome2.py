#! /usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()# 定义要打开的浏览器
dr.get('https://www.jd.com')
sleep(2)
dr.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[1]/div/ul/li[2]/a[1]').click()
sleep(2)
ww=dr.window_handles# 获取所有的窗口标识
print(ww)
dr.switch_to_window(ww[1])
sleep(3)
dr.find_element_by_id('hotwords').find_element_by_xpath('/html/body/div[4]/div[5]/a[1]').click()
sleep(2)
ww=dr.window_handles# 获取所有的窗口标识
print(ww)
dr.switch_to_window(ww[2])
sleep(6)
dr.find_element_by_xpath('/html/body/div[4]/div/div[5]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li[1]/a/div/img').click()
sleep(5)
ww=dr.window_handles# 获取所有的窗口标识
print(ww)
dr.switch_to_window(ww[3])
# dr.switch_to.default_content()
print(8)
dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
sleep(2)
# dr.find_element_by_xpath('//*[@id="GotoShoppingCart"]').click()











