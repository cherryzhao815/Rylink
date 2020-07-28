# -*- coding: utf-8 -*-
# @Time     : 2020/7/28 14:07
# @Author   : Zhili
# @FileName : input_code.py
# @Software : PyCharm

def input_code(driver, code):
    l1 = list(code)
    # key={'0':7,'1':8,'2':9,'3':10,'4':11,'5':12,'6':13,'7':14,'8':15,'9':16}
    for i in l1:
        if i == "1":
            driver.press_keycode(8)
        elif i == "2":
            driver.press_keycode(9)
        elif i == "3":
            driver.press_keycode(10)
        elif i == "4":
            driver.press_keycode(11)
        elif i == "5":
            driver.press_keycode(12)
        elif i == "6":
            driver.press_keycode(13)
        else:
            print("1-6之外的数字没了")
