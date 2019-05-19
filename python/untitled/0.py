#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
import xlrd
from src.testcase import HTMLTestRunner


def ss():
    b=[]
    f = xlrd.open_workbook('ww.xls')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        b.append(sheet.row_values(i))
    return b

class qwe(unittest.TestCase):
 asd=ss()

 #
 # def setUp(self):
 #  #  print('登录')
 #  # def tearDown(self):
 #  #  print('退出')

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
     aa=self.denglu(int(self.asd[0][0]),int(self.asd[0][1]))
     self.assertEqual(aa['code'],0)
     # print(123)

 def test_2(self):
     for i in range(1,len(self.asd)):
      bb=self.denglu(int(self.asd[i][0]),int(self.asd[i][1]))
      self.assertNotEqual(bb['code'],0)

     # print(234)
if __name__ == '__main__':
    # unittest.main()

 suit = unittest.TestSuite()
 suit.addTest(unittest.makeSuite(qwe))
 f = open('cc.html', 'wb')
 runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='巩紫阳', description='结果如下')
 runner.run(suit)
 f.close()
