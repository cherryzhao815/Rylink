# -*- coding: utf-8 -*-
# @Time     : 2019/7/414:14
# @Author   : Zhili
# @FileName : cloud_wallet_login_locators.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy


class CloudWalletLoginPageLocators:
    # 手机按钮
    phone_btn = (MobileBy.ID, "com.hufu.qianbao:id/tv_phone")
    # 邮箱按钮
    email_btn = (MobileBy.ID, "com.hufu.qianbao:id/tv_email")

    # 输入手机号
    phone_input = (MobileBy.ID, "com.hufu.qianbao:id/et_input_phone")

    # 点击下一步,登录 用的同一个xpath
    login_btn = (MobileBy.ID, "com.hufu.qianbao:id/bt_login")
    # 输入密码
    pwd_input = (MobileBy.ID, "com.hufu.qianbao:id/et_input_pwd")

    # 验证码登录按钮
    code_login_btn = (MobileBy.ID , "com.hufu.qianbao:id/tv_change_verify")
    hd_wallet = (MobileBy.ID, "com.hufu.qianbao:id/tv_wallet_hd")