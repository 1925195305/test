#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
class qwe(unittest.TestCase):
    def setUp(self):
        print('开始')
# 执行每一个测试用例前执行一次
# 初始化测试环境
    def tearDown(self):
        print('结束')
# 执行灭一个测试用例后执行一次
# 清理测试环境
    def test_1(self):
        a=6+1
        print(123)
        self.assertEqual(a,7)
    def test_2(self):
        b=9-8
        print(456)
        self.assertEqual(b,1)
if __name__=='__main__':
    unittest.main()


# url = "http://120.132.8.33:9000/api/Account/GetAllDiseaseInfo"
#
# payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n"
# headers = {
#     'Content-Type': "application/json",
#     'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#     'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#     'Language': "zh_CN",
#     'APIVersion': "3.0",
#     'User-Agent': "PostmanRuntime/7.11.0",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "4ce0a4c7-9549-405f-86c4-5ecac0855894,1064b0fd-e300-4678-808f-518907452ae7",
#     'Host': "120.132.8.33:9000",
#     'accept-encoding': "gzip, deflate",
#     'content-length': "152",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("GET", url, data=payload, headers=headers)
# import json
#
# # res=response.text
# res=response.json()
# # msg=json.loads(res)
# if res['code']== 0:
#     print('成功')
