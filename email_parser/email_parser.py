#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/4/26 20:05
# @Author  : Nana Xing
# @File    : email_parser.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :

from selenium import webdriver
import time


class EmailParser:
    def __init__(self, email=None):
        self.time_sleep = 2  # 时间间隔
        self.time_shift = 0  # 时间偏移(相对于服务器)

        self.url = 'http://www.yopmail.com/zh/'
        self.loginname = '+++++'  # 163邮箱账号
        self.password = '*****'  # 密码

    def login(self):
        # 在webdriver.Chrome()的括号内添加相应的webdriver的路径信息
        # 如果不添加路径信息就得把相应的webdriver放到python的安装文件夹
        browser = webdriver.Chrome()
        browser.get(self.url)
        browser.maximize_window()  # 窗口最大化
        time.sleep(3)
        browser.find_elements_by_css_selector('')
        browser.switch_to.frame('x-URS-iframe')  # 切换到登录框
        browser.find_element_by_name('email').clear()
        browser.find_element_by_name('email').send_keys(self.loginname)
        browser.find_element_by_name('password').clear()
        browser.find_element_by_name('password').send_keys(self.password)
        browser.find_element_by_id('dologin').click()
        time.sleep(3)
        browser.switch_to_default_content()  # 退出登录框
        time.sleep(3)
        browser.switch_to.frame('x-URS-iframe')  # 进入确认登录框
        browser.find_element_by_link_text("继续登录").click()
        time.sleep(20)
        browser.quit()


if __name__ == "__main__":
    email = EmailParser()
    email.login()
