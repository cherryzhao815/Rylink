# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 11:10
# @Author   : Zhili
# @FileName : quick_transaction.py
# @Software : PyCharm

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.otc_locators import OtcLocators as loc
from HooAppUIProject.PageLocators.otc_locators import select_coin


class QuickTransaction(BasePage):
    def click_buy_tab(self):
        name = "点击购买tab"
        self.wait_ele_visible(locator=loc.quciky_buy_tab, doc=name)
        self.click_element(locator=loc.quciky_buy_tab, doc=name)

    def click_sell_tab(self):
        name = "点击出售tab"
        self.wait_ele_visible(locator=loc.quciky_sell_tab, doc=name)
        self.click_element(locator=loc.quciky_sell_tab, doc=name)

    def select_coin(self, coin_name):
        name = "选择购买币种"
        self.wait_ele_visible(locator=select_coin(coin_name), doc=name)
        self.click_element(locator=select_coin(coin_name), doc=name)

    def switch_buy_ways(self):
        name = "切换购买方式"  # 在测试用例中需要先判断当前的购买方式之后再切换
        self.wait_ele_visible(locator=loc.switch_buy_way, doc=name)
        self.click_element(locator=loc.switch_buy_way, doc=name)

    def input_quantity_amount(self, amount):
        name = "输入购买或者出售数量或金额"
        self.wait_ele_visible(locator=loc.input_amount, doc=name)
        self.input_text(locator=loc.input_amount, text=amount, doc=name)

    def click_buy_btn(self):
        name = "点击购买按钮"
        self.wait_ele_visible(locator=loc.click_buy, doc=name)
        self.click_element(locator=loc.click_buy, doc=name)

    def click_sell_btn(self):
        name = "点击出售按钮"
        self.wait_ele_visible(locator=loc.click_sell, doc=name)
        self.click_element(locator=loc.click_sell, doc=name)

    def select_pay_method(self):
        name = "选择单价最优的支付方式"
        self.wait_ele_visible(locator=loc.select_payment, doc=name)
        self.click_element(locator=loc.select_payment, doc=name)

    def click_buy_ok_btn(self):
        name = "点击出售确定按钮"
        self.wait_ele_visible(locator=loc.click_buy_ok_btn, doc=name)
        self.click_element(locator=loc.click_buy_ok_btn, doc=name)

    def click_sell_ok_btn(self):
        name = "点击出售确定按钮"
        self.wait_ele_visible(locator=loc.click_sell_ok_btn, doc=name)
        self.click_element(locator=loc.click_sell_ok_btn, doc=name)

    # def input_trans_password(self):
    #     name = "输入交易密码"

    # self.find_element_by_xpath(
    #     "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout[1]")
    # base_driver.press_keycode(10)
    # base_driver.press_keycode(11)
    # base_driver.press_keycode(12)
    # base_driver.press_keycode(13)
    # base_driver.press_keycode(14)
    # base_driver.press_keycode(15)
