# -*- encoding=utf8 -*-
from airtest.core.api import *
from unity.base.base_page import BasePage
import allure


class IrrigationPage(BasePage):

    def _switch_logic(self, area_name):
        self.simple_touch(
            Template(r"../images/tpl_btn_irrigation_on.png", record_pos=(0.3, -0.1), resolution=(1920, 1080)))
        self.simple_sleep(10.0)
        self.simple_snapshot(msg=f"开启{area_name}灌溉状态")
        self.simple_touch(
            Template(r"../images/tpl_btn_irrigation_off.png", record_pos=(0.3, 0.0), resolution=(1920, 1080)))
        self.simple_sleep(1.0)
        self.simple_snapshot(msg=f"关闭{area_name}灌溉状态")

    @allure.step("执行灌溉系统测试")
    def test_irrigation_system(self):
        self.simple_touch(
            Template(r"../images/tpl_btn_water_status.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_sleep(1.0)

        # 区域A测试
        self.simple_touch(
            Template(r"../images/tpl_btn_irrigation_on.png", record_pos=(0.3, -0.1), resolution=(1920, 1080)))
        self.simple_sleep(3.0)
        self.simple_touch(
            Template(r"../images/tpl_btn_irrigation_off.png", record_pos=(0.3, 0.0), resolution=(1920, 1080)))
        self.simple_sleep(3.0)
        self.simple_snapshot(msg="选中区域A")

        # 退出逻辑
        self.simple_touch(Template(r"../images/tpl_btn_view_area.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_sleep(1.0)
        self.simple_touch(Template(r"../images/tpl_btn_exit_water.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_snapshot(msg="退出回到主界面")