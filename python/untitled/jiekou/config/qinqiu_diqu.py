#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests
def denglu_diqu(self):

    url = "http://120.132.8.33:9000/api/Others/GetCountryList"

    payload = ""
    headers = {
        'Content-Type': "application/json",
        'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
        'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
        'Language': "zh_CN",
        'APIVersion': "3.0",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "e201f15c-c894-4d89-a4ad-deaa8d99d056,72a05ddc-dab4-496d-a6e3-d7922727e58f",
        'Host': "120.132.8.33:9000",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, data=payload, headers=headers)
    res = response.json()
    return res

