#!/user/bin/python
#!-*- coding:utf-8 -*-
# 第一步导入appium模块webdriver类
# from appium import  webdriver
# from time import sleep
# # 面向过程
# # 测试脚本与appium服务器进行连接的参数数据
# a = {
#       "platformName": "Android",
#       "platformVersion": "5.1.1",
#       "deviceName": "emulator-5554",
#       "appPackage": "com.qk.butterfly",
#       "appActivity": ".main.LauncherActivity"
# }
# # 测试脚本是appium服务器与手机建立连接的过程,dr变量就是appium的服务器
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=a)
# sleep(20.0)
# # # 元素是ID，就是使用ID地位方法
# # # dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
# # # 获取微信文字
# # # 元素的多级定位
# # # 先地位上一级，在定位下面的元素。没有ID，找class属性
# # text=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# # print(text)
# # # 插入等待时间
# # sleep(3.0)
# # # 退出APP，包括后台程序也退出
# # dr.quit()
# # textwx=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# # textwb = dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# # textqq = dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# # textpasswd = dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# # print(textwx)
# # print(textwb)
# # print(textqq)
# # print(textpasswd)
# # sleep(3.0)
# # dr.quit()
# # 登陆,send_keys()输入的是字符串
# # 2 clickable ---》true
# # 3 enabled ---》 true
# # 4 foucsable --》 true
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15103819460')
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('13137246872zls')
# sleep(5.0)
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(10.0)
# dr.quit()
# from appium import webdriver
# from time import sleep
# class zidong(object):
#     # zidong类是连接手机APP的参数
#     a = {
#           "platformName": "Android",
#           "platformVersion": "5.1.1",
#           "deviceName": "emulator-5554",
#           "appPackage": "com.qk.butterfly",
#           "appActivity": ".main.LauncherActivity"
#     }
#     def __init__(self):
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.a)
#     def check_text(self):
#         textwx = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name(
#             'android.widget.TextView').text
#         print(textwx)
#         return textwx
#     def close_app(self):
#         self.dr.quit()
# if __name__=='__main__':
#     go  = zidong()
#     sleep(10.0)
#     go.check_text()
#     sleep(10.0)
#     go.close_app()
# from appium import webdriver
# from time import sleep
# import unittest
# class zidong(unittest.TestCase):
#     # zidong类是连接手机APP的参数
#     a = {
#           "platformName": "Android",
#           "platformVersion": "5.1.1",
#           "deviceName": "emulator-5554",
#           "appPackage": "com.qk.butterfly",
#           "appActivity": ".main.LauncherActivity"
#     }
#     def setUp(self):
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.a)
#     def test_1(self):
#         sleep(10.0)
#         textwx = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name(
#             'android.widget.TextView').text
#         print(textwx)
#         self.assertEqual(textwx,'微信')
#     def tearDown(self):
#         self.dr.quit()
# if __name__=='__main__':
#     # 忽略一个警告
#     # unittest.main(verbosity=2,warnings=True)
#     unittest.main()
# from appium import webdriver
# import time
# import unittest
# class ceshi(unittest.TestCase):
#     a = {
#               "platformName": "Android",
#               "platformVersion": "5.1.1",
#               "deviceName": "emulator-5554",
#               "appPackage": "com.qk.butterfly",
#               "appActivity": ".main.LauncherActivity"
#         }
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
#     def test_wx(self):
#         time.sleep(10.0)
#         textwx = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name(
#             'android.widget.TextView').text
#         self.assertEqual(textwx,'微信')
#     def test_qq(self):
#         time.sleep(10.0)
#         textqq = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name(
#             'android.widget.TextView').text
#         self.assertEqual(textqq,'QQ')
#     def test_wb(self):
#         time.sleep(10.0)
#         textwb = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name(
#             'android.widget.TextView').text
#         self.assertEqual(textwb,'微博')
#     def test_mm(self):
#         time.sleep(10.0)
#         textpasswd = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name(
#             'android.widget.TextView').text
#         self.assertEqual(textpasswd,'密码')
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
# if __name__ == '__main__':
#     unittest.main()
# from appium import webdriver
# from time import sleep
# class zidong(object):
#     a = {
#           "platformName": "Android",
#           "platformVersion": "5.1.1",
#           "deviceName": "emulator-5554",
#           "appPackage": "com.qk.butterfly",
#           "appActivity": ".main.LauncherActivity"
#     }
#     dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
#     def jump(self):
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#     def login(self,phone,password):
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
#         sleep(10.0)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#         sleep(5.0)
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(10.0)
#     def close_app(self):
#         self.dr.quit()
# if __name__  ==  '__main__':
# 创建类的实例，go就是类的实例
#     go = zidong()
#     go.jump()
#     go.login('15103819460','13137246872zls')
#     go.close_app()
# from time import sleep
# import unittest
# from appium import webdriver
# class ce(unittest.TestCase):
#     a = {
#                   "platformName": "Android",
#                   "platformVersion": "5.1.1",
#                   "deviceName": "emulator-5554",
#                   "appPackage": "com.qk.butterfly",
#                   "appActivity": ".main.LauncherActivity"
#             }
#     @classmethod
#     # cls表示类的实例，cls、self，都可以表示类的实例
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
#     def join(self,name,password):
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
#         sleep(10.0)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#         sleep(5.0)
#         print('准备登陆')
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(10.0)
#     def test_1(self):
#         self.join('15103819460','13137246872zls')
#         print('开始断言')
#         sleep(10)
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
#         self.assertEqual(text,'热门')
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
# if __name__ == '__main__':
#     unittest.main()
# from time import sleep
# import unittest
# from appium import webdriver
# class ce(unittest.TestCase):
#     a = {
#                   "platformName": "Android",
#                   "platformVersion": "5.1.1",
#                   "deviceName": "emulator-5554",
#                   "appPackage": "com.qk.butterfly",
#                   "appActivity": ".main.LauncherActivity"
#             }
#     @classmethod
#     # cls表示类的实例，cls、self，都可以表示类的实例
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
#     def join(self,name,password):
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#         sleep(10)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
#         sleep(10.0)
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#         sleep(5.0)
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(10.0)
#     # def test_1(self):
#     #     self.join('15103819460','13137246872zls')
#     #     sleep(10)
#     #     text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
#     #     self.assertEqual(text,'热门')
#     def logout(self):
#         # .find_elements_by_class_name() 定位一个class属性的元素，要求该元素唯一
#         # .find_element_by_class_name()  定位一个class属性的元素，元素多个
#         data =self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
#         data[0].click()
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
# if __name__ == '__main__':
#     unittest.main()
# from appium import webdriver
# from time import sleep
# a = {
#                   "platformName": "Android",
#                   "platformVersion": "5.1.1",
#                   "deviceName": "emulator-5554",
#                   "appPackage": "com.qk.butterfly",
#                   "appActivity": ".main.LauncherActivity"
#             }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(10)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15103819460')
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('13137246872zls')
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(10.0)
# # 通过列表获取要点击的模块
# n  = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# n[3].click()
# # 模拟人工上划
# # 获取当前屏幕的分辨率
# size = dr.get_window_size()
# x1 = size['width'] * 0.5 #x轴 50
# y1 = size['height'] * 0.25 # 起始y坐标
# y2 = size['height'] * 0.75 # 150
# # 上划屏幕
# for i in range(2):
#     dr.swipe(x1,y2,x1,y1)
# # 点击设置
# dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
# sleep(5.0)
# dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
# sleep(10.0)
# dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
from appium import webdriver
from time import sleep
import unittest
class qwe(unittest.TestCase):
  a = {
                    "platformName": "Android",
                    "platformVersion": "5.1.1",
                    "deviceName": "emulator-5554",
                    "appPackage": "com.qk.butterfly",
                    "appActivity": ".main.LauncherActivity"
              }
  @classmethod
  def setUpClass(cls):
    cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.a)
  def join(self, name, password):
    sleep(10)
    self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
    sleep(10)
    self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
    sleep(10.0)
    self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
    sleep(5.0)
    print('准备登陆')
    self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
    sleep(10.0)
  def quit(self):
    n = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
    n[3].click()
    size = self.dr.get_window_size()
    x1 = size['width'] * 0.5
    y1 = size['height'] * 0.25
    y2 = size['height'] * 0.75
    for i in range(2):
        self.dr.swipe(x1,y2,x1,y1)
    self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
    sleep(5.0)
    self.dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
    sleep(10.0)
    self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
  def test_1(self):
    self.join('15103819460','13137246872zls')
    text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
    self.assertEqual(text,'热门')
    self.quit()
  def test_2(self):
    self.join('15103819460', '13137246872zls')
    text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
    self.assertEqual(text, '热门')
    self.quit()
  @classmethod
  def tearDownClass(cls):
    cls.dr.quit()
if __name__ == '__main__':
    unittest.main()