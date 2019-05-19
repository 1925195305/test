#! /usr/bin/python
#-*- coding:utf-8 -*-

# selenium:wab自动化测试工具集
# 开源免费，支持多浏览器，

from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()# 定义要打开的浏览器
# dr.get('http://www.baidu.com')# 请求网页
# sleep(2)
# dr.get('https://i.qq.com')
# sleep(5)

dr.switch_to.frame('login_frame')# 定位到框架

dr.switch_to_default_content()# 退出框架，退出到最初的页面

dr.switch_to.parent_frame()# 切换到上一个框架


# sleep(2)
# dr.find_element_by_id('img_out_1925195305').click()


# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1925195305')
# sleep(2)
# dr.find_element_by_id('p').send_keys('lvgzy13792846211')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(5)


# dr.switch_to.default_content()
# dr.find_element_by_xpath('//*[@id="tb_logout"]').click()
# sleep(5)
# qw=dr.switch_to_alert()
# qw.accept()







# dr.switch_to.default_content()
# dr.find_element_by_id('composebtn').click()
# sleep(2)
# dr.find_element_by_id('toAreaCtrl').send_keys('15518117087@163.com')
# sleep(2)
# dr.find_element_by_id('subject').send_keys('你好，啊')
# sleep(2)
# dr.find_element_by_css_selector('html').send_keys('hahahhaha')
# sleep(2)
# dr.find_element_by_name('sendbtn').click()
# sleep(2)

# dr.get('http://www.jd.com')
# sleep(2)
# dr.back()# 回到上一次打开的网页
# sleep(2)
# dr.forward()# 前进
# dr.find_element_by_id('kw').send_keys('python')
# sleep(2)

# # dr.find_element_by_id('su').click()# 通过id定位

# dr.find_element_by_class_name('mnva')# 通过class,为了区分python中class

# dr.find_element_by_name('tj_trnews').click()# 通过name定位

# dr.find_element_by_link_text('贴吧')# link_text 文本定位

# dr.find_element_by_partial_link_text('贴')# 模糊文本定位

# dr.find_element_by_tag_name('')# tag_name 通过标签页定位

# dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[5]').click()# 路径标记语言，右键复制选择xpath

#
# dr.find_element_by_css_selector('a.mnav:nth-child(5)').click()# css 定位


# dr.find_elements_by_id('')# 定位多个

# 层级定位：先定位一个大元素，再定位一个子元素




# 定位之后的动作： 1.send_keys 输入
#                 2.click 点击
#                 3.clear 清除
#                 4.text  文本


# dr.quit()# 关闭浏览器

# 获取网页标题,一般用作断言，

# print(dr.title)# 判断请求的网页的标题是否符合预期结果

# print(dr.current_url)# 获取请求网址

# dr.set_window_size(800,500)# 设置浏览器窗口大小

# dr.set_window_position(400,400)# 设置浏览器窗口位置

# dr.maximize_window()# 最大化浏览器

# dr.minimize_window()# 最小化浏览器

