#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
from src.testcase import HTMLTestRunner


class qwe(unittest.TestCase):
 def denglu(self,user,password):
  url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

  payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(user,password)
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
  res=response.json()
  return res

 def test_1(self):
     aa=self.denglu(15993835273,111111)
     self.assertEqual(aa['code'],0)

 def test_2(self):
     bb=self.denglu(1599383527,111111)
     self.assertNotEqual(bb['code'],0)

 def test_3(self):
     cc=self.denglu(15993835273,11111)
     self.assertEqual(cc['code'],0)
if __name__ == '__main__':

 #    创建一个测试套件
 suit =unittest.TestSuite()
 # 将测试用例添加到套件中
 # suit.addTest(qwe('test_1'))
 # suit.addTest(qwe('test_2'))
 # suit.addTest(qwe('test_3'))
 suit.addTest(unittest.makeSuite(qwe))
 # 将qwe类中所有test开头的函数都添加到测试套件中

 f=open('zxc.html','wb')
 # 定义测试报告的信息
 runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='巩紫阳', description='结果如下')
 runner.run(suit)
 f.close()



