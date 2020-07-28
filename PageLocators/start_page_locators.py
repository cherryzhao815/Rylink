# -*- coding: utf-8 -*-
# @Time     : 2019/7/414:10
# @Author   : Zhili
# @FileName : start_page_locators.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy


class StartPageLocators:
    cloud_wallet = (MobileBy.ID, "com.hufu.qianbao:id/tv_wallet_clound")
    hd_wallet = (MobileBy.ID, "com.hufu.qianbao:id/tv_wallet_hd")
