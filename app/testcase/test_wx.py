#!/user/bin/python
#!-*- coding:utf-8 -*-
import unittest
from app_test.testcase import HTMLTestRunner
from time import sleep
from appium import webdriver
from app_test.func.duqu import wx,wb,qq,mm
from app_test.testcase.logs import get_logger
# 给日志一个变量，g是全局变量
g = get_logger(name='test_wx.py')
# 测试脚本
class Test(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
            a = {
                  "platformName": "Android",
                  "platformVersion": "5.1.1",
                  "deviceName": "emulator-5554",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity"
            }
            cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
            sleep(10)
            g.info('app建立连接完成')
      @classmethod
      def tearDownClass(cls):
            cls.dr.quit()
            g.info('app关闭')
      def test_wx(self):
            # 微信测试用例
            g.info('执行测试')
            text = wx(self.dr)
            self.assertEqual(text,'微信')
      def test_wb(self):
            # 微博测试用例
            g.info('执行测试')
            text = wb(self.dr)
            self.assertEqual(text,'微博')
      def test_qq(self):
            # qq测试用例
            g.info('执行测试')
            text = qq(self.dr)
            self.assertEqual(text,'QQ')
      def test_mm(self):
            # 微博测试用例
            g.info('执行测试')
            text = mm(self.dr)
            self.assertEqual(text,'密码')
if __name__ == '__main__':
      suite = unittest.TestSuite()
      suite.addTest(Test('test_wx'))
      suite.addTest(Test('test_wb'))
      suite.addTest(Test('test_qq'))
      suite.addTest(Test('test_mm'))
      f = open('abc.html','wb')
      runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告',  # verbosity为2时更详细
                                             tester='张路生', description='结果如下', verbosity=2
                                             )
      runner.run(suite)