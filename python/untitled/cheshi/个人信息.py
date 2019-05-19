#! /usr/bin/python
#-*- coding:utf-8 -*-

import requests
import unittest
class qwe(unittest.TestCase):
    def gerenxinxi(self):

        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","countryGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038"}

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            # 'accessToken': "59702a4e2b034907a1f7545a4f0424e3",
            # 'User-Agent': "PostmanRuntime/7.11.0",
            # 'Accept': "*/*",
            # 'Cache-Control': "no-cache",
            # 'Postman-Token': "2acd2fba-b169-487c-9160-9156e3ad8aba,e0654220-55e6-4005-9f3d-32082570ea8f",
            # 'Host': "120.132.8.33:9000",
            # 'accept-encoding': "gzip, deflate",
            # 'Connection': "keep-alive",
            # 'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res = response.json()
        return res

    # print(response.text)
    def test_1(self):
        self.gerenxinxi()
    def test_2(self):
        self.assertNotEqual(['code'],0)
if __name__ == '__main__':
 unittest.main()
