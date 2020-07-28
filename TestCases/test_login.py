# -*- coding: utf-8 -*-
# @Time     : 2020/7/23 9:41
# @Author   : Zhili
# @FileName : test_login.py
# @Software : PyCharm


import pytest

from HooAppUIProject.PageObjects.HomePage.home_page_objects import HomePage
from HooAppUIProject.PageObjects.LoginRegisterPageObjects.login_register_page_objects import LoginRegisterPage
import time

@pytest.mark.usefixtures("base_driver")
class TestLogin:
    def test_login_success(self, base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入用户名，输入密码，点击登录
        LoginRegisterPage(base_driver).input_tel_box("13751030137")
        LoginRegisterPage(base_driver).input_password_box("zzl815815")
        LoginRegisterPage(base_driver).click_login_btn()
        time.sleep(5)
        # 断言:判断首页 - 是否还有登录/注册按钮
        assert HomePage(base_driver).is_loginRegisterBtn_exist() == False

    # def test_otc(self, base_driver):
    #     pass
