# -*- encoding=utf8 -*-
from airtest.core.api import *
from unity.base.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step("执行登录操作")
    def login(self, username, password):
        # 注意：图片路径请根据实际存放位置调整，这里保留原样或建议改为相对路径
        self.simple_touch(
            Template(r"../images/tpl_input_username.png", record_pos=(0.0, -0.1), resolution=(1920, 1080)))
        self.simple_text(username)
        self.simple_sleep(1.0)

        self.simple_touch(
            Template(r"../images/tpl_input_password.png", record_pos=(0.0, 0.05), resolution=(1920, 1080)))
        self.simple_text(password)

        self.simple_touch(Template(r"../images/tpl_btn_login.png", record_pos=(0.0, 0.2), resolution=(1920, 1080)))
        self.simple_sleep(2.0)
        self.simple_snapshot(msg="登录操作完成")

        self.simple_assert_exists(
            Template(r"../images/tpl_btn_cruise_free.png", record_pos=(0.4, 0.0), resolution=(1920, 1080)),
            "验证通过：场景中已显示主界面")