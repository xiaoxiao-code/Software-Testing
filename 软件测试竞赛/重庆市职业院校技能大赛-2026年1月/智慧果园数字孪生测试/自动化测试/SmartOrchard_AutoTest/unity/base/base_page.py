from airtest.core.api import *
import os


class BasePage:
    def __init__(self):
        # 确保图片路径正确，这里假设图片都在项目根目录的 images 文件夹下
        # 实际使用时建议配置 ST.PROJECT_ROOT
        pass

    def simple_touch(self, template_obj):
        touch(template_obj)

    def simple_text(self, content):
        text(content)

    def simple_sleep(self, seconds):
        sleep(seconds)

    def simple_snapshot(self, msg=""):
        snapshot(msg=msg)

    def simple_assert_exists(self, template_obj, msg):
        assert_exists(template_obj, msg)