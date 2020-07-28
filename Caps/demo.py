#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/12/21 21:18

import yaml
import os
#打开yaml文件
fs = open(os.getcwd()+ "/caps.yaml",encoding="utf-8")
#使用yaml的load()函数
obj = yaml.load(fs)
print(obj)