# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:32
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.baseAction import Baseaction


# 下面这个类里面存放所有 我的 界面模型测试时需要使用的动作
class MinePageAction(Baseaction):
    # 将 myself 界面中会用到的元素特征都准备好
    login_re = By.ID, "com.tpshop.malls:id/head_img"
    mobile_input = By.ID, "com.tpshop.malls:id/mobile_et"
    pwd_input = By.ID, "com.tpshop.malls:id/pwd_et"
    agree_btn = By.ID, "com.tpshop.malls:id/agree_btn"
    login_tv = By.ID, "com.tpshop.malls:id/login_tv"

    # 点击 登录/注册  的动作
    def click_login_re(self):
        self.click(self.login_re)

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
        self.click(self.login_tv)


