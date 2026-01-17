# -*- encoding=utf8 -*-
from airtest.core.api import *
from unity.base.base_page import BasePage
import allure


class PeoplePage(BasePage):

    @allure.step("执行人员流动查看测试")
    def check_people_flow(self):
        self.simple_touch(
            Template(r"../images/tpl_btn_people_flow.png", record_pos=(0.35, 0.1), resolution=(1920, 1080)))
        self.simple_assert_exists(
            Template(r"../images/tpl_label_li.png", record_pos=(0.4, 0.0), resolution=(1920, 1080)),
            "验证通过：场景中已显示人员标签")
        self.simple_sleep(4.0)
        self.simple_snapshot(msg="人员流动全景视角")

        self.simple_touch(Template(r"../images/tpl_label_li.png"))
        self.simple_sleep(3.0)
        self.simple_snapshot(msg="人员-李XX")

        self.simple_touch(Template(r"../images/tpl_label_wang.png"))
        self.simple_sleep(3.0)
        self.simple_snapshot(msg="人员-王XX")

        self.simple_touch(Template(r"../images/tpl_label_visitor.png"))
        self.simple_sleep(3.0)
        self.simple_snapshot(msg="人员-游客")