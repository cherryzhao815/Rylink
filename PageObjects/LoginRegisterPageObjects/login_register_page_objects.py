# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 10:43
# @Author   : Zhili
# @FileName : login_register_page_objects.py
# @Software : PyCharm

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.login_register_page_locators import LoginRegisterLocators as loc


class LoginRegisterPage(BasePage):
    def input_tel_box(self, tel):
        name = "输入手机号码"
        self.wait_ele_visible(locator=loc.input_phone, doc=name)
        self.input_text(locator=loc.input_phone, text=tel, doc=name)

    def input_password_box(self, pwd):
        name = "输入密码"
        self.wait_ele_visible(locator=loc.input_pwd, doc=name)
        self.input_text(locator=loc.input_pwd, text=pwd, doc=name)

    def click_login_btn(self):
        name = "点击登录按钮"
        self.wait_ele_visible(locator=loc.bt_login, doc=name)
        self.click_element(locator=loc.bt_login, doc=name)

    def click_agree_box(self):
        name = "勾选同意复选框"
        self.wait_ele_visible(locator=loc.iv_select, doc=name)
        self.click_element(locator=loc.iv_select, doc=name)
