#!/user/bin/python
#!-*- coding:utf-8 -*-
import os
# 获取当前.py文件的路径
a = os.path.dirname(os.path.abspath(__file__))
print(a)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 项目的根目录
LOG_DIR = BASE_DIR + r'\logs'
# 报告目录
REPORT_DIR = BASE_DIR + r'\report'
# 源文件的目录
SRC_DIR = BASE_DIR + r'\src'
#测试用例目录
TEST_CASE = BASE_DIR + r'\testcase'
# 页面方法目录
FUNC = BASE_DIR + r'\func'
# 公共目录
UNTIL = BASE_DIR + r'\until'
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
# # 清除输入框
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
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
