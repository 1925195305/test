#! /usr/bin/python
#-*- coding:utf-8 -*-
import requests

# class geren():
def denglu_geren(self):
    url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

    querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","targetUserGuid":"2fdd90a6-25f2-11e9-a4d7-0242ac120003"}

    payload = ""
    headers = {
    'Content-Type': "application/json",
    'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
    'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
    'Language': "zh_CN",
    'APIVersion': "3.0",
    'accessToken': "61817a3eded744fea464f57a455103bf",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "36202f26-d38e-48c7-990c-03bcd7793b48,23722a39-68ed-4efd-9c29-13f61ad6c9f3",
    'Host': "120.132.8.33:9000",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    res = response.json()
    return res



