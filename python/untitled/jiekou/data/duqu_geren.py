#! /usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
def denlu_shuju():
    shuj=[]
    f = xlrd.open_workbook(r'C:\Users\gzy\Desktop\untitled\jiekou\data\geren.xls')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        shuj.append(sheet.row_values(i))
    return shuj
