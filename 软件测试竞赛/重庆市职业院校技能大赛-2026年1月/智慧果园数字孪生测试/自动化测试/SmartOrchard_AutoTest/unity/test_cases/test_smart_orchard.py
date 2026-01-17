# -*- encoding=utf8 -*-
import pytest
import allure
import os
from airtest.core.api import *
from unity.pages.login_page import LoginPage
from unity.pages.cruise_page import CruisePage
from unity.pages.view_page import ViewPage
from unity.pages.people_page import PeoplePage
from unity.pages.irrigation_page import IrrigationPage

# 配置APP路径
APP_PATH = r"C:\Users\jack\Desktop\IntelliOrchardUnity_Data\IntelliOrchardUnity.exe"

@allure.feature("智慧果园数字孪生系统测试")
class TestSmartOrchard:

    def setup_class(self):
        # 初始化Airtest和设备
        auto_setup(__file__)
        if not G.DEVICE_LIST:
            auto_setup(__file__, devices=["Windows:///"])

        # 启动应用
        start_app(APP_PATH)
        sleep(4.0)  # 等待Unity启动
        snapshot(msg="软件启动成功")

        # 初始化页面对象
        self.login_page = LoginPage()
        self.cruise_page = CruisePage()
        self.view_page = ViewPage()
        self.people_page = PeoplePage()
        self.irrigation_page = IrrigationPage()

    def teardown_class(self):
        # 关闭应用
        os.system(r"C:\Windows\System32\taskkill.exe /f /im IntelliOrchardUnity.exe")

    @allure.story("全流程场景测试")
    @allure.title("智慧果园系统全流程自动化测试")
    def test_full_workflow(self):
        """
        执行顺序：登录 -> 巡航 -溉
        """

        # 步骤1：系统登录
        with allure.step("步骤1：执行管理员登录"):
            self.login_page.login("administrator", "123456")

        # 步骤2：无人机巡航
        with allure.step("步骤2：执行无人机巡航"):
            self.cruise_page.cruise_free_test()
            self.cruise_page.cruise_fixed_test()

        # 步骤3：自由视角
        with allure.step("步骤3：执行视角滚轮缩放测试"):
            self.view_page.view_scroll_action()

        # 步骤4：人员管理
        with allure.step("步骤4：执行人员标签查看测试"):
            self.people_page.check_people_flow()

        # 步骤5：水肥灌溉
        with allure.step("步骤5：执行灌溉系统开关与区域切换测试"):
            self.irrigation_page.test_irrigation_system()

if __name__ == "__main__":
    # 调试用
    pytest.main(["-s", "-v", "test_smart_orchard.py"])