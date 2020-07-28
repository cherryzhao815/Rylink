#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: xiaojian
# Time: 2018/11/26 21:18

import logging

from logging.handlers import RotatingFileHandler

import time
from HooAppUIProject.Common import get_path

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
handler_2 = RotatingFileHandler(get_path.logs_dir + "/App_Autotest_{0}.log".format(curTime), backupCount=20,
                                encoding='utf-8')
# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

# logging.info("hehehe")
# logging.debug("debug")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

"""
python日志级别:
critical>error>waring>info>debug
级别越高打印的日志越少，反之亦然，即
Debug : 打印全部的日志(notset等同于debug)
info : 打印info,warning,error,critical级别的日志
warning : 打印warning,error,critical级别的日志
error : 打印error,critical级别的日志
critical : 打印critical级

将log记录保存在文件的FileHandler
将log输出到屏幕的StreamHandler
支持日志根据时间回滚的TimedRotatingFileHandler
根据文件大小回滚的RotatingFileHandler等等（回滚不太好理解，根据时间或文件大小回滚其实就是根据时间或者文件大小来保存日志，比如只保存3天的日志，超过3天的就自动删除，或者设置日志文件只能为一定大小，超过就删除）
"""

