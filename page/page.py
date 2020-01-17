# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:52
from page.page_home import EnterPageAction
from page.page_mine import MinePageAction


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def inithomepage(self):
        return EnterPageAction(self.driver)

    @property
    def initminepage(self):
        return MinePageAction(self.driver)
