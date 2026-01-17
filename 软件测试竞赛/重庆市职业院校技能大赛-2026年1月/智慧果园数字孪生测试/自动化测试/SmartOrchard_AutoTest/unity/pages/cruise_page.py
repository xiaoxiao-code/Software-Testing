# -*- encoding=utf8 -*-
from airtest.core.api import *
from unity.base.base_page import BasePage
import allure


class CruisePage(BasePage):

    def long_press_key(self, key_name, duration=3.0):
        """模拟长按键盘按键"""
        dev = device()
        dev.key_press(key_name)
        sleep(duration)
        dev.key_release(key_name)
        sleep(1.0)

    @allure.step("执行自由巡航测试")
    def cruise_free_test(self):
        self.simple_touch(
            Template(r"../images/tpl_btn_cruise_free.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))

        self.long_press_key("w", 3.0)
        self.simple_snapshot(msg="无人机向前飞行3秒后位置")

        self.long_press_key("s", 3.0)
        self.simple_snapshot(msg="无人机向后飞行3秒后位置")

        self.long_press_key("a", 3.0)
        self.simple_snapshot(msg="无人机向左飞行3秒后位置")

        self.long_press_key("d", 3.0)
        self.simple_snapshot(msg="无人机自由巡航测试结束")

    @allure.step("执行定点巡航测试")
    def cruise_fixed_test(self):
        # 你的原代码这里点了两次，保留原逻辑
        self.simple_touch(
            Template(r"../images/tpl_btn_cruise_fixed.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_touch(
            Template(r"../images/tpl_btn_cruise_fixed.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_sleep(5.0)
        self.simple_snapshot(msg="无人机定点巡航")