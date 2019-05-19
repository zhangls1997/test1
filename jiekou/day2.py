#!/user/bin/python
#!-*- coding:utf-8 -*-
# import xlrd
# ff = xlrd.open_workbook('b.xls')
# sheet = ff.sheets()[0]
# c = sheet.nrows
# a = []
# d = []
# for i in range(c):
#     b = sheet.row_values(i)
#     if type(b[0]) == str or type(b[1]) == str:
#         a.extend(b)
#         continue
#     d.extend(b)
# print(a)
# print(d)
# import xlrd
# class abc(object):
#     def shuju(self):
#         ff = xlrd.open_workbook('b.xls')
#         sheet = ff.sheets()[0]
#         c = sheet.nrows
#         a = []
#         for i in range(c):
#             b = sheet.row_values(i)
#             a.append(b)
#         return a
# import HTMLTestRunner
# import requests
# import unittest
# import xlrd
# def shuju():
#     ff = xlrd.open_workbook('b.xls')
#     sheet = ff.sheets()[0]
#     c = sheet.nrows
#     data = []
#     for i in range(c):
#         print(i)
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
#     # 创建一个测试套件
#     suit = unittest.TestSuite()
#     # 将测试用例添加到测试套件中中
#     # suit.addTest(qwe('test_1'))
#     # suit.addTest(qwe('test_2'))
#     # qwe是类的名字
#     # 将qwe类中所有以test开头的函数都添加到测试套件中
#     suit.addTest(unittest.makeSuite(qwe))
#     #打开一个空文件（yi.HTML为后缀名）
#     f = open('abc.html','wb')
#     #定义测试报告的信息
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',
#                                            tester='张路生',description='结果如下',
#                                            )
#     #suit是测试套件变量
#     runner.run(suit)
#     f.close()
# import requests
# import unittest
# import xlrd
# def read():
#     ff = xlrd.open_workbook('b.xls')
#     sheet = ff.sheets()[0]
#     c = sheet.nrows
#     data = []
#     for i in range(c):
#         b = sheet.row_values(i)
#         data.append(b)
#     return data
# class school(unittest.TestCase):
#     data = read()
#     def send(self,address):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         querystring = {"filterInput":"{}".format(address)}
#         payload = ""
#         headers = {
#             'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#             'Accept-Encoding': '[{"key":"Accept-Language","value":" zh-CN,zh;q=0.9","type":"text","enabled":true,"description":""}]',
#             'Accept-Language': "zh-CN,zh;q=0.9",
#             'Cache-Control': "max-age=0",
#             'Connection': "keep-alive",
#             'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#             'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#             'Postman-Token': "e9601d14-837c-4a7a-8f1b-c55298a8955d,68d84637-0202-4045-a9e2-e68797e94ffa",
#             'Host': "testsupport-be.haofenshu.com",
#             'cache-control': "no-cache"
#             }
#         response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#         res = response.json()
#         return res
#     def test_chaxun(self):
#         qq = self.send(self.data[0][0])
#         self.assertEqual(qq['code'],0)
#     def test_wxchaxun(self):
#         for i in range(len(self.data)):
#             if i < len(self.data)-1:
#                 ww = self.send(self.data[i+1][0])
#                 self.assertEqual(ww['code'],1)
# if __name__=='__main__':
#     unittest.main()
# import xlwt
# ff = xlwt.Workbook(encoding='utf-8')
# sheet = ff.add_sheet('123')
# sheet.write(0,0,'我爱你')
# ff.save('aa.xls')