# -*- coding: utf-8 -*-
# @Time     : 2020/7/23 14:43
# @Author   : Zhili
# @FileName : home_page_locators.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy


class HomePageLocators:
    # 首页登录注册按钮
    login_register_btn = (
        MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_login_register']")
    # 法币按钮
    otc_btn = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_otc']")
    # 关闭小程序
    iv_close = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_close']")