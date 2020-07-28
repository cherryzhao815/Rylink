# -*- coding: utf-8 -*-
# @Time     : 2020/7/23 14:37
# @Author   : Zhili
# @FileName : home_page_locators.py
# @Software : PyCharm

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.home_page_locators import HomePageLocators as loc


class HomePage(BasePage):
    # 点击登陆注册按钮
    def click_LoginRegister_Btn(self):
        name = "点击登陆注册按钮"
        self.wait_ele_visible(locator=loc.login_register_btn, doc=name)
        self.click_element(locator=loc.login_register_btn, doc=name)

    # 存在则True，不存在则False
    def is_loginRegisterBtn_exist(self):
        name = "首页_登陆按钮是否存在"
        self.wait_ele_visible(locator=loc.login_register_btn, doc=name)
        try:
            self.get_element(locator=loc.login_register_btn, doc=name)
            return True
        except:
            return False

    # 点击法币
    def click_otc_btn(self):
        name = "点击法币小程序"
        self.wait_ele_visible(locator=loc.otc_btn, doc=name)
        self.click_element(locator=loc.otc_btn, doc=name)
