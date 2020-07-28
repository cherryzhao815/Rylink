# -*- coding: utf-8 -*-
# @Time     : 2020/7/27 11:15
# @Author   : Zhili
# @FileName : otc_locators.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy


# 选择币种
def select_coin(coin_name):
    select_coin_xpath = (MobileBy.XPATH, "//android.widget.TextView[@text='" + coin_name + "']")
    return select_coin_xpath


class OtcLocators:
    # 点击快捷购买tab
    quciky_buy_tab = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_buy']")

    quciky_sell_tab = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_sell']")
    # 购买方式：按照数量还是金额
    switch_buy_way = (
        MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/ll_switch_buy_way']")
    # 输入购买数量或金额
    input_amount = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_amount']")

    # 点击购买  "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_buy']"
    click_buy = (MobileBy.XPATH,
                 "//android.support.v4.view.ViewPager[@resource-id='com.hufu.qianbao:id/viewPager']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")

    click_sell = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_buy' and @text='出售']")
    # 选择支付方式（单价最优）
    select_payment = (MobileBy.XPATH,
                      "//android.support.v7.widget.RecyclerView[@resource-id='com.hufu.qianbao:id/recyclerView']/android.widget.LinearLayout[1]")
    # 确认购买页面，“购买”按钮
    click_buy_ok_btn = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_buy']")
    # 确认出售页面，“出售”按钮
    click_sell_ok_btn = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_sell']")

    # 确认购买页面，“返回”按钮
    click_back_btn = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_1']")
    # 输入交易密码
    input_trans_code = (
        MobileBy.XPATH,
        "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout[1]")

    # 订单详情页面，点击返回或者关闭小程序按钮，弹出框页面
    # 我确认未付款给对方
    checked_cb_otc = (MobileBy.XPATH, "//android.widget.CheckBox[@resource-id='com.hufu.qianbao:id/cb_otc']")
    click_cancel = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_cancel']")
    click_ok = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_ok']")
