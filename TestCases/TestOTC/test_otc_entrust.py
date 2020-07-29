import pytest
from HooAppUIProject.PageObjects.OtcPageObjects.release_entrust import release_entrust
from HooAppUIProject.PageObjects.HomePage.home_page_objects import HomePage
import time

pay_password ="000000"

@pytest.mark.usefixtures('is_logined')
class TestOTCEntrust:

    # 固定价格--购买委托
    def test_fixed_entrust_buy(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).click_buy_tab()
        release_entrust(is_logined).input_price_amount(7,100)
        release_entrust(is_logined).input_quantity_amount(50)
        release_entrust(is_logined).select_pay_method()
        release_entrust(is_logined).click_relsease_enrtust()
        release_entrust(is_logined).input_trans_password(pay_password) # 输入交易密码

    # 固定价格--购买委托
    def test_fixed_entrust_sell(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).click_sell_tab()
        release_entrust(is_logined).input_price_amount(7, 100)
        release_entrust(is_logined).input_quantity_amount(50)
        release_entrust(is_logined).click_relsease_enrtust()
        release_entrust(is_logined).input_trans_password(pay_password) # 输入交易密码

    # 浮动价格--购买委托
    def test_float_entrust_buy(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).click_buy_tab()
        release_entrust(is_logined).input_yijia_amount("-0.5",6,100)
        release_entrust(is_logined).input_quantity_amount(50)
        release_entrust(is_logined).select_pay_method()
        release_entrust(is_logined).click_relsease_enrtust()
        release_entrust(is_logined).input_trans_password(pay_password)  # 输入交易密码

    # 浮动价格--购买委托
    def test_float_entrust_sell(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).click_sell_tab()
        release_entrust(is_logined).input_yijia_amount("2", 7, 100)
        release_entrust(is_logined).input_quantity_amount(50)
        release_entrust(is_logined).click_relsease_enrtust()
        release_entrust(is_logined).input_trans_password(pay_password)  # 输入交易密码

    # 编辑委托--默认第一个
    def test_edit_entrust(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).input_edit_entrust()
        release_entrust(is_logined).click_relsease_enrtust()
        release_entrust(is_logined).input_trans_password(pay_password)  # 输入交易密码

    # 撤单委托单
    def test_cancel_entrust(self, is_logined):
        HomePage(is_logined).click_otc_btn()  # 点击法币小程序
        release_entrust(is_logined).cancel_entrust_order()