# -*- coding: utf-8 -*-
# @Time     : 2019/7/110:18
# @Author   : Zhili
# @FileName : slide_verify.py
# @Software : PyCharm
import base64
import random
import time

from PIL import Image
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SlideVerify:

    def __init__(self, driver):
        self.driver = driver

    # 进入模拟拖动流程
    def slide_verify(self):
        # 等待验证框的出现
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, '//canvas[@class="geetest_canvas_slice geetest_absolute"]')))
        # 刷新一下极验图片
        element = self.driver.find_element_by_xpath('//a[@class="geetest_refresh_1"]')
        element.click()
        time.sleep(1)

        # 保存两张图片
        self.save_img('full.jpg', 'geetest_canvas_fullbg')
        self.save_img('cut.jpg', 'geetest_canvas_bg')
        full_image = Image.open('full.jpg')
        cut_image = Image.open('cut.jpg')

        # 根据两个图片计算距离
        distance = self.get_offset_distance(cut_image, full_image)

        # 开始移动
        self.start_move(distance)

        # 如果出现error
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="geetest_slider geetest_error"]')))
            print("验证失败")
            return
        except TimeoutException as e:
            print(e)

        # 判断是否验证成功
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="geetest_slider geetest_success"]')))
        except TimeoutException:
            print("again times")
            self.slide_verify()
        else:
            print("验证成功")

    def save_img(self, img_name, class_name):
        # js_study 语句，返回image
        getImgJS = 'return document.getElementsByClassName("' + class_name + '")[0].toDataURL("image/png");'
        img = self.driver.execute_script(getImgJS)
        base64_data_img = img[img.find(',') + 1:]
        image_base = base64.b64decode(base64_data_img)
        file = open(img_name, 'wb')
        file.write(image_base)
        file.close()

    # 判断颜色是否相近
    def is_similar_color(self, x_pixel, y_pixel):
        for i, pixel in enumerate(x_pixel):
            if abs(y_pixel[i] - pixel) > 50:
                return False
        return True

    # 计算距离
    def get_offset_distance(self, cut_image, full_image):
        for x in range(cut_image.width):
            for y in range(cut_image.height):
                cpx = cut_image.getpixel((x, y))
                fpx = full_image.getpixel((x, y))
                if not self.is_similar_color(cpx, fpx):
                    img = cut_image.crop((x, y, x + 50, y + 40))
                    # 保存一下计算出来位置图片，看看是不是缺口部分
                    img.save("1.png")
                    return x

    # 开始移动
    def start_move(self, distance):
        element = self.driver.find_element_by_xpath('//div[@class="geetest_slider_button"]')

        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        distance -= element.size.get('width') / 2
        distance += 25

        # 按下鼠标左键
        ActionChains(self.driver).click_and_hold(element).perform()
        time.sleep(0.5)
        while distance > 0:
            if distance > 10:
                # 如果距离大于10，就让他移动快一点
                span = random.randint(5, 8)
            else:
                # 快到缺口了，就移动慢一点
                span = random.randint(2, 3)
            ActionChains(self.driver).move_by_offset(span, 0).perform()
            distance -= span
            time.sleep(random.randint(10, 50) / 100)

        ActionChains(self.driver).move_by_offset(distance, 1).perform()
        ActionChains(self.driver).release(on_element=element).perform()
