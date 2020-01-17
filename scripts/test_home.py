# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 15:42
import pytest

from base import init_driver
from page.page import Page
pytestmark = pytest.mark.skip("跳过")


class TestDemo:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_auto_intohome(self):
        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.enter_home()

