# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 13:52
import os
import time

import pytest

from base import init_driver
from page.page import Page
from base.analysis import getData


class TestDemo:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # 定义一个 test 函数来对应我们测试用例中执行结果为 “账号不存在” 的那一类用例
    @pytest.mark.parametrize("args", getData("test_login_not"))
    def test_login_not(self, args):
        # 使用 首页模型当中的进入 首页的动作
        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.enter_home()
        self.page.inithomepage.click_mine()
        time.sleep(2)

        # 判断是否登录
        if self.page.initminepage.logged_on():
            print("已登录，将退出登录")
            self.page.initminepage.click_Logging_out()

        # 点击登录注册按钮
        print("未登录，即将登录")
        self.page.initminepage.click_login_reg()
        time.sleep(2)
        # 输入账号
        self.page.initminepage.input_id(args[0])
        # 输入密码
        self.page.initminepage.input_pwd(args[1])
        # 点击允许协议
        self.page.initminepage.click_agree()
        # 点击登录
        self.page.initminepage.click_login_enter()
        # 测试登录点击之后的toast 获取
        tt_content = self.page.initminepage.is_toast_exist([2])

        if tt_content == True:
            self.driver.get_screenshot_as_file(os.getcwd()+os.sep+'img/01.png')
            print("截图")
        # 添加断言
        assert tt_content
