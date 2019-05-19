#!/user/bin/python
#!-*- coding:utf-8 -*-
import os
import logging
import datetime
#
logs = os.path.join(r'D:\zls\app_test\logs',str(datetime.datetime.now().date())+".out")
# print(logs)
# 创建一个日志文件
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
# print(formatter)
# 日志输出到控制台
con_handler = logging.StreamHandler()
# 加载日志格式
con_handler.setFormatter(formatter)
# 将日志输出到文本
fil_handler = logging.FileHandler(logs,encoding='utf-8')
# 加载日志格式
fil_handler.setFormatter(formatter)
# 定义日志登记，设置日志句柄，供其他对象调用
fil_handler.setFormatter(formatter)
def get_logger(name):
    # 获取脚本的名字传入到日志
    logger = logging.getLogger(name)
    # 加入一个手柄
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    # 设置日志的等级,INFO四级，包含以上三级，不包含建议级
    logger.setLevel(logging.INFO)
    return logger
go  = get_logger('logs.py')
go.info('start')