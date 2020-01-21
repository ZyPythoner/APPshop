# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:32
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.baseAction import Baseaction


# 下面这个类里面存放所有 我的 界面模型测试时需要使用的动作
class MinePageAction(Baseaction):
    # 将 myself 界面中会用到的元素特征都准备好
    nick_name_tv = By.XPATH, "text,登录/注册,1"  # 登录/注册
    login_reg = By.ID, "com.tpshop.malls:id/head_img"  # 头像
    mobile_input = By.ID, "com.tpshop.malls:id/mobile_et"  # 手机
    pwd_input = By.ID, "com.tpshop.malls:id/pwd_et"  # 密码
    agree_btn = By.ID, "com.tpshop.malls:id/agree_btn"  # 协议
    login_tv = By.ID, "com.tpshop.malls:id/login_tv"  # 登录按钮
    setting_btn = By.ID, "com.tpshop.malls:id/setting_btn"  # 设置按钮
    exit_tv = By.ID, "com.tpshop.malls:id/exit_tv"  # 安全退出按钮

    # 点击 登录/注册  的动作
    def click_login_reg(self):
        self.click(self.login_reg)

    # 在账号框中转入账号的动作
    def input_id(self, value):
        self.input_txt(self.mobile_input, value)

    # 在密码框中输入 密码 的动作
    def input_pwd(self, value):
        self.input_txt(self.pwd_input, value)

    # 点击允许协议
    def click_agree(self):
        self.click(self.agree_btn)

    # 点击登录的 动作
    def click_login_enter(self):
        imgfile = open('./img/01.png', 'rb').read()
        allure.attach(imgfile, '截图', allure.attachment_type.PNG)
        self.click(self.login_tv)

    # 捕捉 登录/注册 是否找到
    def logged_on(self):
        try:
            self.find_element(self.nick_name_tv)
            print("F")
            return False
        except Exception:
            print("T")
            return True

    # 安全退出账号
    def click_Logging_out(self):
        self.click(self.setting_btn)
        time.sleep(2)
        self.click(self.exit_tv)