#! /usr/bin/python
#-*- coding:utf-8 -*-
import yaml
import unittest
with open(r'C:\Users\gzy\Desktop\untitled\src\element\iten.yaml','r',encoding='utf-8') as fb:
    # a=yaml.load(fb)使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data=yaml.load(fb,Loader=yaml.FullLoader)
    # print(item_data)
    # print()
def wx(driver):
    # dr=''
    text= driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    # text.assertEqual(text, '微信')
    # print(text)
    return text
def wb(driver):
    # dr=''
    text=driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    # text2.assertEqual(text2, '微博')
    # print(text2)
    return text
def qq(driver):
    # dr=''
    text=driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    # text3.assertEqual(text3, 'QQ')
    # print(text3)
    return text
def mm(driver):
    # dr=''
    text=driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    # text4.assertEqual(text4, '密码')
    # print(text4)
    return text
