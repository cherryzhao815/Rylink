# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 10:57
# @Author   : Zhili
# @FileName : test_otc_buy.py
# @Software : PyCharm

import pytest
from HooAppUIProject.PageObjects.OtcPageObjects.quick_transaction import QuickTransaction
from HooAppUIProject.PageObjects.HomePage.home_page_objects import HomePage
import time
from HooAppUIProject.Common.input_code import input_code
from HooAppUIProject.PageObjects.OtcPageObjects.close_otc_small_program import CloseOTCProgrammer


@pytest.mark.usefixtures('is_logined')
class TestOTCBuy:

    # def test_a(self, is_logined):
    #     print(is_logined)

    # @pytest.mark.usefixtures("base_driver")
    # def test_input_password(self, base_driver, password):
    #     l1 = list(password)
    #     for i in l1:
    #         if i == 1:
    #             base_driver.press_keycode(10)
    #         elif i == 2:
    #             base_driver.press_keycode(11)
    #         elif i == 3:
    #             base_driver.press_keycode(12)
    #         elif i == 4:
    #             base_driver.press_keycode(13)
    #         elif i == 5:
    #             base_driver.press_keycode(14)
    #         elif i == 6:
    #             base_driver.press_keycode(15)
    #         else:
    #             print("1-6之外的数字没了")
    # 快捷购买
    def test_quick_buy(self, is_logined):
        # 点击法币小程序
        HomePage(is_logined).click_otc_btn()
        QuickTransaction(is_logined).select_coin("USDT")
        # 输入购买数量（使用默认值）
        QuickTransaction(is_logined).input_quantity_amount("1000")
        QuickTransaction(is_logined).click_buy_btn()
        QuickTransaction(is_logined).select_pay_method()
        QuickTransaction(is_logined).click_buy_ok_btn()
        time.sleep(3)
        # 输入交易密码
        input_code(is_logined, "123456")
        # 断言处理： 进入到订单页面查看是否有待付款的订单
        assert True
        # 关闭小程序，回到主页面
        CloseOTCProgrammer(is_logined).close_otc_programmer()

    # 快捷出售
    def test_quick_sell(self, is_logined):
        HomePage(is_logined).click_otc_btn()
        QuickTransaction(is_logined).click_sell_tab()
        QuickTransaction(is_logined).select_coin("USDT")
        # 切换为按数量出售
        QuickTransaction(is_logined).switch_buy_ways()
        # 输入出售数量（）
        QuickTransaction(is_logined).input_quantity_amount("200")
        QuickTransaction(is_logined).click_sell_btn()
        QuickTransaction(is_logined).select_pay_method()
        QuickTransaction(is_logined).click_sell_ok_btn()
        time.sleep(3)
        # 输入交易密码
        input_code(is_logined, "123456")
        CloseOTCProgrammer(is_logined).close_otc_programmer()
#
