# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 13:52
import time

from base import init_driver
from page.page import Page


class TestDemo:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # 定义一个 test 函数来对应我们测试用例中执行结果为 “账号不存在” 的那一类用例
    def test_login_f(self):
        # 使用 首页模型当中的进入 首页的动作
        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.enter_home()
        self.page.inithomepage.click_mine()
        time.sleep(2)
        # 点击登录注册按钮
        self.page.initminepage.click_login_re()
        time.sleep(2)
        # 输入账号
        self.page.initminepage.input_id("18887654321")
        # 输入密码
        self.page.initminepage.input_pwd("123456qq")
        # 点击允许协议
        self.page.initminepage.click_agree()
        # 点击登录
        self.page.initminepage.click_login_enter()
        # 测试登录点击之后的toast 获取
        tt_content = self.page.initminepage.get_toast_content("成功")
        # 添加断言
        assert tt_content == "账号不存在!"
