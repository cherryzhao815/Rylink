# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 10:40
# @Author   : Zhili
# @FileName : login_register_page_locators.py
# @Software : PyCharm
from appium.webdriver.common.mobileby import MobileBy


class LoginRegisterLocators:
    # 登录页面请输入手机号输入框
    input_phone = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_phone']")
    # 登录页面请输入密码输入框
    input_pwd = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_pwd']")
    # 登录页面“登录”按钮
    bt_login = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/bt_login']")
    # 登录页面 “手机”按钮
    tv_phone = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_phone']")
    # 登录页面“email”按钮
    ll_email = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/ll_email']")
    # email输入框
    input_email = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_email']")
    # 获取验证码
    send_phonecode = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_phonecode']")
    # 验证码输入框
    input_code = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_code']")

    # 登录页面 切换国家
    tv_area = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_area']")
    # 显示登录密码
    iv_pwd_on = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_pwd_on']")
    # 关闭密码显示
    iv_pwd_off = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_pwd_off']")
    # 忘记密码？
    tv_forget_pwd = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_forget_pwd']")
    # 切换登录方式：验证码还是密码登录
    tv_change_verify = (
        MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_change_verify']")
    # 密码登录

    # 立即注册
    register_immediately_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='立即注册']")
    # 切换语言
    tv_language = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_language']")

    # 选择语言 //android.widget.TextView[@text='简体中文']
    def select_language(self, language):
        """
        :param language: 简体中文,English,繁體中文,한국어
        :return: //android.support.v7.widget.RecyclerView[@resource-id='com.hufu.qianbao:id/recyclerView']/android.widget.RelativeLayout[1]
        """
        res = (MobileBy.XPATH, "//android.widget.TextView[@text='" + language + "']")
        return res

    # 返回X
    iv_left_back = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_left_back']")
    iv_select = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_select']")

