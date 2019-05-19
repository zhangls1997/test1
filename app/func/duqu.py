#!/user/bin/python
#!-*- coding:utf-8 -*-
import yaml
import unittest
with open(r'D:\zls\app_test\element\data.yaml','r',encoding='utf-8') as fb:
    # a=yaml.load(fb)使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data=yaml.load(fb,Loader=yaml.FullLoader)
def wx(driver):
    text= driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def wb(driver):
    text=driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def qq(driver):
    text=driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def mm(driver):
    text=driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    return text