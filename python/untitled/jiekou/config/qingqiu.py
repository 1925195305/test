#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
from jiekou.data.duqu import shuju
class jiekou_qinqiu():
# class wind(unittest.TestCase):
    def denglu(self, user, password):
        # sj = shuju()
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}" % (user, password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            # 'Postman-Token': "aca4eac6-e259-49b5-9a51-d7cb753132e2,076623e9-1952-405e-8e76-004813867150",
            # 'Host': "120.132.8.33:9000",
            # 'accept-encoding': "gzip, deflate",
            # 'content-length': "150",
            # 'Connection': "keep-alive",
            # 'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        return res
if __name__=='__main__':

    shu = shuju()
    for i in range(len(shu)):
        a =jiekou_qinqiu().denglu(int(shu[i][0]), int(shu[i][1]))
        print(a)

