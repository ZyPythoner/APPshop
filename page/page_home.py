# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:52
import time

from selenium.webdriver.common.by import By

from base.baseAction import Baseaction


class EnterPageAction(Baseaction):
    # 允许按钮
    allow_bt = By.ID, "com.android.packageinstaller:id/permission_allow_button"
    # 进入按钮
    into_bt = By.ID, "com.tpshop.malls:id/start_img"
    # 主页-我的
    home_index = By.ID, "com.tpshop.malls:id/mine_ll"

    def auto_enter_home(self):
        try:
            time.sleep(2)
            self.find_element(self.home_index)
            print("点击检测——>>>欢迎进入主页")
        except Exception:
            # 点击四次允许操作
            for i in range(4):
                self.click(self.allow_bt)
                time.sleep(0.6)
            print("点击完成")

    def enter_home(self):
        try:
            time.sleep(2)
            self.find_element(self.home_index)
            print("滑动检测——>>>欢迎进入主页")
        except Exception:
            # 执行三次向左滑屏操作
            for i in range(3):
                self.swipe_left()
                time.sleep(0.6)
            # 点击进入主页的按钮
            self.click(self.into_bt)
            print("滑动完成")

    def click_mine(self):
        self.click(self.home_index)


