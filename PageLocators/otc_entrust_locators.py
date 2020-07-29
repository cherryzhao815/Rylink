# @Author   : xiaoxie
from appium.webdriver.common.mobileby import MobileBy

class Otc_entrust_Locators:
    """发布委托元素"""

    ck_entrust_in = (MobileBy.XPATH, "//android.widget.TextView[@text='发布委托']")  # 点击发布委托入口
    ck_buy = (MobileBy.ID,"tv_buy")  # 购买
    ck_sell = (MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]")  # 出售
    switch_coin =(MobileBy.ID,"tv_coin") # 发布委托的币种

    # 固定价格
    ck_fixed_price =(MobileBy.ID,"tv_fixed_price") # 固定价格
    ipt_fixed_price =(MobileBy.XPATH,"//*[@resource-id='com.hufu.qianbao:id/et_danjia']") # 输入单价
    ipt_fixed_zuidi =(MobileBy.XPATH,"//*[@resource-id='com.hufu.qianbao:id/et_zuidi']") # 输入最低额
    ipt_fixed_number =(MobileBy.XPATH,"//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_shuliang']") # 请输入购买数量
    ipt_fixed_amount =(MobileBy.XPATH,"//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_jine']") # 请输入购买金额

    # 浮动价格
    ck_float_price = (MobileBy.ID, "tv_float_price")  # 浮动价格
    ck_float_yijia = (MobileBy.ID, "et_yijia")  # 溢价
    ck_float_lowest_price = (MobileBy.ID, "et_lowest_price")  # 请输入最低价
    ck_float_zuidi = (MobileBy.ID, "et_zuidi")  # 输入最低额
    ck_float_number = (MobileBy.ID, "et_shuliang")  # 请输入购买数量
    ck_float_amount = (MobileBy.ID, "et_jine")  # 请输入购买金额

    # 限制时间
    ck_time_limit =(MobileBy.ID,"tv_time_limit") # 点击限制时间
    ck_time_select =(MobileBy.ID,"tv_time_selected") # 点击选择时间
    st_week_2 =(MobileBy.ID,"tv_week_2") # 选择周二
    ipt_start_time =(MobileBy.ID,"tv_start_time") # 开始时间
    ipt_end_time =(MobileBy.ID,"tv_end_time") # 结束时间
    ck_confirm_ok =(MobileBy.ID,"tv_ok") # 点击确定

    st_pay_method =(MobileBy.ID,"tv_pay_method_select") # 选择付款方式
    ck_pay_zfb =(MobileBy.XPATH,"//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_zfb']") # 支付宝
    ck_pay_weixin =(MobileBy.XPATH,"//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_weixin']") # 微信
    ck_pay_bank =(MobileBy.XPATH,"//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_bank']") # 银行卡
    ck_close_pay =(MobileBy.ID,"iv_close") # 关闭弹窗

    ipt_content =(MobileBy.ID,"et_content") # 备注信息
    ck_enter =(MobileBy.ID,"tv_enter") # 点击发布

    ipt_verify_code = (MobileBy.ID, 'tv_0')  # 输入交易密码
    # 关闭小程序
    iv_close = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_close']")

    # 切换到订单界面
    ck_order =(MobileBy.XPATH,"//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/tabbar']/android.widget.RelativeLayout[3]")
    ck_my_entrust = (MobileBy.XPATH,"//android.widget.TextView[@text='我的委托']")
    ck_edit_entrust =(MobileBy.XPATH,"//*[@resource-id='com.hufu.qianbao:id/tv_edit']")
    ck_cancel_order =(MobileBy.XPATH,"//*[@resource-id='com.hufu.qianbao:id/tv_cancel_order']")
    ck_ok_cancel =(MobileBy.XPATH,"//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_right']")