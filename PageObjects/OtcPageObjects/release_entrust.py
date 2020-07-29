# @Author   : xiaoxie

from HooAppUIProject.Common.base_page import BasePage
from HooAppUIProject.PageLocators.otc_entrust_locators import Otc_entrust_Locators as otc_en
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class release_entrust(BasePage):

    def click_buy_tab(self):
        """默认发布购买委托"""
        self.wait_ele_visible(otc_en.ck_entrust_in)
        self.click_element(otc_en.ck_entrust_in)

    def click_sell_tab(self):
        """出售委托"""
        self.wait_ele_visible(otc_en.ck_entrust_in)
        self.click_element(otc_en.ck_entrust_in)
        time.sleep(2)
        self.click_element(otc_en.ck_sell)

    def input_yijia_amount(self, yijia, lowest_price,zuidi_price):
        '''浮动价格--输入溢价、最低价、最低额'''
        self.wait_ele_visible(otc_en.ck_float_price)
        self.click_element(otc_en.ck_float_price)
        self.wait_ele_visible(otc_en.ck_float_yijia) # 输入溢价
        self.input_text(otc_en.ck_float_yijia, yijia)
        self.input_text(otc_en.ck_float_lowest_price, lowest_price)  # 输入最低价
        self.input_text(otc_en.ck_float_zuidi, zuidi_price)  # 输入最低额
        self.sys_hide_keyboard()
        self.swipe_up()

    def input_price_amount(self,price,Min_amount):
        '''固定价格--输入单价、最低额'''
        self.wait_ele_visible(otc_en.ipt_fixed_price)
        self.clear_loc_text(otc_en.ipt_fixed_price)
        self.input_text(otc_en.ipt_fixed_price,price)
        self.input_text(otc_en.ipt_fixed_zuidi,Min_amount)

    def input_quantity_amount(self,quantity):
        '''输入数量、返回金额'''
        self.wait_ele_visible(otc_en.ipt_fixed_number)
        self.click_element(otc_en.ipt_fixed_number)
        self.input_text(otc_en.ipt_fixed_number,quantity)
        self.sys_hide_keyboard()
        self.swipe_up()

    def select_pay_method(self):
        '''选择付款方式'''
        self.click_element(otc_en.st_pay_method)
        self.wait_ele_visible(otc_en.ck_pay_zfb)
        self.click_element(otc_en.ck_pay_zfb)
        self.click_element(otc_en.ck_pay_weixin)
        self.click_element(otc_en.ck_close_pay)

    def input_edit_entrust(self):
        '''编辑委托、输入备注'''
        self.wait_ele_visible(otc_en.ck_order)
        self.click_element(otc_en.ck_order)
        self.click_element(otc_en.ck_my_entrust)
        time.sleep(2)
        self.click_element(otc_en.ck_edit_entrust)
        time.sleep(2)
        self.swipe_up()
        self.sys_hide_keyboard()
        self.clear_loc_text(otc_en.ipt_content)
        self.input_text(otc_en.ipt_content,"我是备注")

    def cancel_entrust_order(self):
        '''撤单'''
        self.wait_ele_visible(otc_en.ck_order)
        self.click_element(otc_en.ck_order)
        self.click_element(otc_en.ck_my_entrust)
        time.sleep(2)
        self.click_element(otc_en.ck_cancel_order)
        time.sleep(1)
        self.click_element(otc_en.ck_ok_cancel)
        self.wait_ele_visible(otc_en.iv_close)
        self.click_element(otc_en.iv_close)

    def click_relsease_enrtust(self):
        '''点击发布'''
        self.click_element(otc_en.ck_enter)

    def input_trans_password(self,pwd):
        '''输入交易密码'''
        time.sleep(2)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(self.driver.find_element(*otc_en.ipt_verify_code)).click().send_keys(
            pwd).perform()  # 输入交易密码
        self.wait_ele_visible(otc_en.iv_close)
        self.click_element(otc_en.iv_close)