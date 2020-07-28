# -*- coding: utf-8 -*-
# @Time     : 2020/7/28 14:25
# @Author   : Zhili
# @FileName : common.py
# @Software : PyCharm

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.home_page_locators import HomePageLocators as loc


class CloseSmallProgram(BasePage):
    def close_small_program(self):
        name = "关闭小程序"
        self.wait_ele_visible(locator=loc.iv_close, doc=name)
        self.click_element(locator=loc.iv_close, doc=name)
