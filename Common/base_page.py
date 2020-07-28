from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

import time
import allure
from HooAppUIProject.Common.get_path import *
from datetime import datetime
from HooAppUIProject.Common.my_log import MyLog
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import win32gui
import win32con
import os

'''页面操作基础方法类'''


class BasePage():
    # def __init__(self,driver=webdriver.Chrome()):
    def __init__(self, driver):
        self.driver = driver

    "web页面操作类"

    # 等待元素可见
    def wait_ele_visible(self, locator, doc="", times=30, poll_frequency=0.5):
        """
        :param locator: 元素定位表达式
        :param doc: 操作的模块名_页面名_操作名（用于异常时截图存储的截图图片名称）
        :param times:等待时间
        :param poll_frequency:轮询间隔时间
        :return:
        """
        MyLog().info('等待元素{}可见'.format(locator))
        try:
            start_time = datetime.now()
            # MyLog().info("等待开始时间{}：".format(start_time))
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))

        except Exception as e:
            MyLog().info('等待元素失败！！！！！！！！！！！！！')
            # 截图
            self.save_screenshot(doc)
            raise e

        end_time = datetime.now()
        # 求等待的差值，写在日志中，等待了多久
        wait_time = (end_time - start_time).seconds
        MyLog().info("wait_time:{}".format(wait_time))
        MyLog().info("等待结束，等待时长为{}秒".format(wait_time))

    # 元素是否可见，可见时返回True，不可见时返回False
    def is_ele_visible(self, locator, doc="", times=30, poll_frequency=0.5):
        """
        :param locator: 元素定位表达式
        :param doc: 操作的模块名_页面名_操作名（用于异常时截图存储的截图图片名称）
        :param times:等待时间
        :param poll_frequency:轮询间隔时间
        :return:
        """
        MyLog().info('等待元素{}可见'.format(locator))
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            # 截图
            self.save_screenshot(doc)
            MyLog().info(e)
            return False

    def wait_element_to_be_click(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        等待元素可点击
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            MyLog.info("开始等待页面元素<{}>是否可点击！".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            MyLog.error("页面元素<{}>等待可点击失败！".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog.info("页面元素<{}>等待可点击，等待时间：{}秒".format(loc, round(end_time - start_time, 2)))

    # 等待元素存在
    def wait_ele_exist(self, locator, doc="", times=30, poll_frequency=0.5):
        """
        :param locator: 元素定位表达式
        :param doc: 操作的模块名_页面名_操作名（用于异常时截图存储的截图图片名称）
        :param times:等待时间
        :param poll_frequency:轮询间隔时间
        :return:
        """
        MyLog().info('等待元素{}存在'.format(locator))
        try:
            # 开始等待时间
            start_time = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.now()
            # 求等待的差值，写在日志中，等待了多久
            wait_time = (end_time - start_time).seconds
            MyLog().info("等待结束，等待时长为{}秒".format(wait_time))
        except:
            MyLog().info('等待元素失败！！！！！！！！！！！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 查找元素
    def get_element(self, locator, doc=""):
        MyLog().info('查找元素{}'.format(locator))
        try:
            # self.wait_ele_visible(*locator)
            ele = self.driver.find_element(*locator)
            # 返回元素对象，以便进行后续操作
            return ele
        except Exception as e:
            MyLog().info('查找元素失败！！！！！！！！！！！！！')
            # 截图
            self.save_screenshot(doc)
            raise e

    # 查找多个元素
    def get_elements(self, locator, doc=""):
        MyLog().info('查找元素{}'.format(locator))
        try:
            eles = self.driver.find_elements(*locator)
            return eles
        except:
            MyLog().info('查找元素失败！！！！！！！！！！！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入内容
    def input_text(self, locator, text, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('向元素{}输入文本{}'.format(locator, text))
        try:
            ele.send_keys(text)
        except:
            MyLog().info('输入文本失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 点击元素
    def click_element(self, locator, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('点击元素{}'.format(locator))
        try:
            ele.click()
        except:
            MyLog().info('点击元素失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 定位表达式指向多个元素，点击指定下标元素
    def click_elements(self, locator, index=0, doc=''):
        eles = self.get_elements(locator, doc)
        try:
            eles[index].click()
            MyLog().info('点击元素{}'.format(locator))
        except:
            MyLog().info('点击元素失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 截屏
    def save_screenshot(self, doc):
        MyLog().info("截取屏幕")
        # 图片名称:模块名_页面名_操作名_时间.png
        file_name = screenshot_dir + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()

        # 截图添加为allure报告的附件
        allure.attach(file, doc, allure.attachment_type.PNG)
        MyLog().info("截取屏幕完成，存放地址在{}".format(file_name))

    # 获取元素文本
    def get_text(self, locator, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('获取元素{}的文本内容'.format(locator))
        try:
            return ele.text
        except:
            MyLog().info('获取元素文本失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 清空元素文本------------------------------------------------
    def clear_loc_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        MyLog().info('清除元素{}的文本内容'.format(locator))
        try:
            ele.clear()
        except:
            MyLog().info('清除元素文本失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, attr, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('获取元素{}的属性'.format(locator))
        try:
            return ele.get_attribute(attr)
        except:
            MyLog.info('获取元素属性失败！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    def get_element_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        '''
        获取WebElement对象的文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值
        '''
        try:
            MyLog.info("在{}中获取元素<{}>的文本值".format(img_doc, loc))
            self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
            text = self.get_element(loc, img_doc).text
        except Exception as e:
            MyLog.error("在{}中获取元素<{}>的文本值失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            MyLog.info("获取到的元素文本值为：{}".format(text))
            return text

    def get_elements_text(self, loc, doc="", timeout=20, poll_frequency=0.5):
        '''
        获取WebElement对象的所有文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值的列表
        '''
        try:
            MyLog.info("在{}中获取元素<{}>的所有文本值".format(doc, loc))
            self.wait_ele_visible(loc, doc, timeout, poll_frequency)
            all_text = self.get_elements(loc, doc)
            text_list = []
            for one_text in all_text:
                text_list.append(one_text.text)
        except Exception as e:
            MyLog.error("在{}中获取元素<{}>的所有文本值失败！".format(doc, loc))
            self.save_screenshot(doc)
            raise e
        else:
            MyLog.info("获取到的元素文本值列表为：{}".format(text_list))
            return text_list

    # 鼠标操作(鼠标悬浮某元素)
    def mosuse_over(self, locator, doc=''):
        # 1、找到要操作的元素
        ele = self.get_element(locator, doc)
        # 2、实例化ActionChains
        ac = ActionChains(self.driver)
        # 3、将要操作的元素添加到actions列表中
        ac.move_to_element(ele)
        # 4、调用perform来操作
        ac.perform()
        # 放在一起写 ActionChains(self.driver).move_to_element(ele).perform()

    '''页面滚动操作'''

    # 滚动元素“底端”与当前窗口的“底部”对齐
    def move_ele_to_baseOfWindow(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)

    # 滚动元素“底端”与当前窗口的“顶部”对齐
    def move_ele_to_topOfWindow(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    # 滚动到页面底部
    def move_to_baseOfWindow(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 滚动到页面底部
    def move_to_topOfWindow(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    # 页面定位到要查看的元素
    def move_to_element(self, locator):
        ele = self.driver.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    '''弹窗处理'''

    def accept_alert(self, times=30, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            MyLog.info('弹窗不存在！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    def dismiss_alert(self, times=30, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except:
            MyLog.info('弹窗不存在！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    # 获取弹窗文本内容
    def get_alert_text(self, times=30, poll_frequency=0.5, doc=''):
        # 等待弹窗存在
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to_alert()
            MyLog().info('弹窗存在，获取弹框的文本内容')
            try:
                return alert.text
            except:
                MyLog.info('获取弹框的文本内容失败！！！！！！！！！！！！！')
                self.save_screenshot(doc)
                raise
        except:
            MyLog.info('弹窗不存在！！！！！！！！！！！！！')
            self.save_screenshot(doc)
            raise

    '''谷歌浏览器--上传文件操作，其他浏览器需要稍作改动'''

    def upload_file(self, filepath):
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # 文本输入框--四级窗口
        edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
        # 打开按钮--二级窗口
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
        # 输入文件地址
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
        # 点击“打开”按钮--提交文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # iframe切换

    # 窗口切换

    # 键盘事件

    "APP页面操作类"

    def sliding_screen(self, direction, img_doc):
        '''
        滑屏操作
        :param direction: 滑屏方向：上-up；下-down；左-left；右-right
        :param img_doc: 截图说明
        :return:
        '''
        size = self.driver.get_window_size()
        try:
            MyLog.info("开始向{}方向滑动".format(direction))
            if direction.lower() == 'up':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.9,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.1,
                                  duration=200)
            elif direction.lower() == 'down':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.1,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.9,
                                  duration=200)
            elif direction.lower() == 'left':
                self.driver.swipe(start_x=size['width'] * 0.9,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.1,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            elif direction.lower() == 'right':
                self.driver.swipe(start_x=size['width'] * 0.1,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.9,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            else:
                MyLog.error("方向选择错误！")
        except Exception as e:
            MyLog.error("向{}方向滑动屏幕失败！".format(direction))
            self.save_screenshot(img_doc)
            raise e

    def switch_to_webview(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        切换到webview页面
        :param loc: webview页面的元素
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            MyLog.info("等待元素{}可见，并进行webview切换".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            cons = self.driver.contexts
            MyLog.info("开始切换到webview：{}".format(cons[-1]))
            self.driver.switch_to.context(cons[-1])
        except Exception as e:
            MyLog.error("切换webview失败！")
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog.info("切换到webview：{}成功，等待时间：{}秒".format(cons[-1], round(end_time - start_time, 2)))

    def switch_to_native_app(self, img_doc):
        '''
        切换到app原生页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            MyLog.info("切换到app原生页面")
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            MyLog.error("切换到app原生页面失败！")
            self.save_screenshot(img_doc)
            raise e

    def application_switching(self, package_name, activity_name, img_doc):
        '''
        应用切换
        :param package_name: 包名
        :param activity_name: 欢迎页面名
        :param img_doc: 截图说明
        :return:
        '''
        try:
            MyLog.info("切换应用到{}".format(package_name))
            self.driver.start_activity(app_package=package_name, app_activity=activity_name)
        except Exception as e:
            MyLog.error("切换应用到{}失败！".format(package_name))
            self.save_screenshot(img_doc)
            raise e

    # 滑屏事件（向上，向下，向左，向右）
    def swipe_up(self, size, time=200, n=1):
        # 向上滑屏
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.75
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.25
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, time)
            sleep(2)
            print('执行滑屏操作')

    def swipe_down(self, size, time=200, n=1):
        # 向下滑屏
        start_x = size["width"] * 0.5
        start_y = size["height"] * 0.25
        end_x = size["width"] * 0.5
        end_y = size["height"] * 0.75
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, time)
            sleep(2)

    def swipe_left(self, size, time=200, n=1):
        # 向左滑屏
        start_x = size["width"] * 0.8
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.2
        end_y = size["height"] * 0.5
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, time)
            sleep(2)

    def swipe_right(self, size, time=200, n=1):
        # 向右滑屏
        start_x = size["width"] * 0.1
        start_y = size["height"] * 0.5
        end_x = size["width"] * 0.9
        end_y = size["height"] * 0.5
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, time)
            sleep(1)

    # 获取屏幕大小
    def get_size(self):
        return self.driver.get_window_size()

    # 获取toast提示信息
    # automationName: UiAutomator2  这样设置caps才能处理toast
    def get_toastMsg(self, str):
        # 1、xpath表达式，文本匹配
        loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format(str))
        # 等待室等待元素存在，不能用等待元素可见
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc).text
        except:
            MyLog.info('没有找到匹配的toast！！！')
            raise

    def quick_sendkeys(self, keys):
        '''快速输入，需要与ADBKeyboard配合使用，提升小程序中的输入效率'''
        sleep(2)
        com = 'adb shell am broadcast -a ADB_INPUT_TEXT --es msg \"%s\"' % keys
        os.system(com)

    # def send_keys(self, keys):
    #     loc = (MobileBy.XPATH,
    #            "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.LinearLayout[1]")
    #     self.driver.find_element(loc).send_keys(keys)

    def action_chains_send_keys(self, locator, text, doc):
        """
        方法使用介绍：ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,
        send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        :param element: 查找的元素
        :param text: 需要输入的信息
        :return:
        """
        a = self.driver.find_element(locator, doc)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(text).perform()



