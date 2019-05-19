#!/user/bin/python
#!-*- coding:utf-8 -*-
# import requests
# # import json
# url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
# # payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"
# # headers = {
# #     'Content-Type': "application/json",
# #     'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
# #     'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
# #     'Language': "zh_CN",
# #     'APIVersion': "3.0",
# #     'User-Agent': "PostmanRuntime/7.11.0",
# #     'Accept': "*/*",
# #     'Cache-Control': "no-cache",
# #     'Postman-Token': "29e3eb16-3c73-4fd6-aa99-1f1e6a64f1c6,48e2d08d-3ee9-40c5-b628-af3d65130209",
# #     'Host': "120.132.8.33:9000",
# #     'accept-encoding': "gzip, deflate",
# #     'content-length': "150",
# #     'Connection': "keep-alive",
# #     'cache-control': "no-cache"
# #     }
# response = requests.request("POST", url, data=payload, headers=headers)
# # res = response.text
# # msg = json.loads(res)
# # if msg['code']== 0:
# #     print("OK")
# res = response.json()
# if res['code'] == 0:
#     print("OK")
# import unittest
# import requests
# class main(unittest.TestCase):
#     def setUp(self):   #执行
#         print('开始')
#     def tearDown(self):  #结束
#         print('结束')
#     def test_1(self):
#        a = 4+5
#        print('123')
#        self.assertEqual(a,9)
#     def test_2(self):
#         b = 6 - 5
#         print('456')
#         self.assertEqual(b,1)
# if __name__=='__main__':
#     unittest.main()
# import requests
# import unittest
# import xlrd
# def shuju():
#     ff = xlrd.open_workbook('b.xls')
#     sheet = ff.sheets()[0]
#     c = sheet.nrows
#     data = []
#     for i in range(c):
#         b = sheet.row_values(i)
#         data.append(b)
#     return data
# class qwe(unittest.TestCase):
#     data = shuju()
#     def denglu(self,user,passwd):
#         url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#         payload = "{\r\n    \"phone\":\"%d\",\r\n    \"password\":\"%d\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(user,passwd)
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'User-Agent': "PostmanRuntime/7.11.0",
#             'Accept': "*/*",
#             'Cache-Control': "no-cache",
#             'Postman-Token': "29e3eb16-3c73-4fd6-aa99-1f1e6a64f1c6,a326873b-7598-46ae-8523-dae1c13df32b",
#             'Host': "120.132.8.33:9000",
#             'accept-encoding': "gzip, deflate",
#             'content-length': "150",
#             'Connection': "keep-alive",
#             'cache-control': "no-cache"
#             }
#         response = requests.request("POST", url, data=payload, headers=headers)
#         res = response.json()
#         return res
#     def test_1(self):
#         for i in range(len(self.data)):
#             if i < len(self.data)-1:
#                 qq = self.denglu(int(self.data[i+1][0]),int(self.data[i+1][1]))
#                 self.assertNotEqual(qq['code'],0)
#     def test_2(self):
#         ee = self.denglu(int(self.data[0][0]),int(self.data[0][1]))
#         self.assertEqual(ee['code'],0)
# if __name__ == '__main__':
#     unittest.main()
# import requests
# import unittest
# class main(unittest.TestCase):
#     def send(self):
#         url = "http://120.132.8.33:9000/api/Account/GetUserInfo"
#         querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","countryGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038"}
#         payload = ""
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'accessToken': "e68c1ff4e50f4596ba961dc306adec63",
#             'User-Agent': "PostmanRuntime/7.11.0",
#             'Accept': "*/*",
#             'Cache-Control': "no-cache",
#             'Postman-Token': "0aafe30a-c0f7-4965-b0f3-e1399f4bf34e,4359fc90-addf-4034-a262-ee57629405cd",
#             'Host': "120.132.8.33:9000",
#             'accept-encoding': "gzip, deflate",
#             'Connection': "keep-alive",
#             'cache-control': "no-cache"
#             }
#         response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#         res = response.json()
#         return res
#     def setUp(self):
#         print('开始')
#     def tearDown(self):
#         print('结束')
#     def test_1(self):
#         qq = self.send()
#         self.assertEqual(qq['code'],0)
#     def test_2(self):
#         ww = self.send()
#         self.assertEqual(ww['msg'],'OK')
#     def test_3(self):
#         ee = self.send()
#         self.assertEqual(ee['data']['sex'],1)
# if __name__ == '__main__':
#     unittest.main()
# class fff(object):
#     def __init__(self,name):
#         self.name=name
#         print(name)
#     def k(self,age,name):
#         print(age)
#         print(name)
# qwe = fff('张三')
# qwe.k(21,'张三')