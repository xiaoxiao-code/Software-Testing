# -*- encoding=utf8 -*-
from airtest.core.api import *
from pywinauto.mouse import scroll
from unity.base.base_page import BasePage
import allure


class ViewPage(BasePage):

    def mouse_scroll_test(self, steps=1):
        """模拟鼠标滚轮操作"""
        center_x, center_y = 960, 540
        # wheel_dist=steps: 1 表示向上滚动一格，-1 表示向下滚动一格
        scroll(coords=(center_x, center_y), wheel_dist=steps)
        sleep(5.0)

    @allure.step("执行自由视角滚轮测试")
    def view_scroll_action(self):
        self.simple_touch(Template(r"../images/tpl_btn_view_free.png", record_pos=(0.35, 0.0), resolution=(1920, 1080)))

        self.mouse_scroll_test(steps=1)
        self.simple_snapshot(msg="自由视角-滚轮向上滑动1格")

        self.mouse_scroll_test(steps=-3)
        self.simple_snapshot(msg="自由视角-滚轮向下滑动复原")