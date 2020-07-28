# -*- coding: utf-8 -*-
# @Time     : 2020/7/28 16:40
# @Author   : Zhili
# @FileName : close_otc_small_program.py
# @Software : PyCharm

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.otc_locators import OtcLocators as loc
from HooAppUIProject.PageLocators.home_page_locators import HomePageLocators


class CloseOTCProgrammer(BasePage):
    def close_otc_programmer(self):
        name = "关闭小程序"
        self.wait_ele_visible(locator=HomePageLocators.iv_close, doc=name)
        self.click_element(locator=HomePageLocators.iv_close, doc=name)
        ele = self.get_element(locator=loc.checked_cb_otc, doc=name)
        if ele:
            self.click_element(locator=loc.checked_cb_otc, doc=name)
            self.click_element(locator=loc.click_ok, doc=name)
        else:
            pass
