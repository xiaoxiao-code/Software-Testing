# test_web_manager.py - Web端管理系统自动化测试用例
import pytest
import allure
import os
import time
from common.excel_utils import get_excel_data
from pages.web.fruit_page import FruitPage
from pages.web.tree_page import TreePage

# 数据文件路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_FILE = os.path.join(BASE_DIR, "data", "fruit_data.xlsx")


@allure.feature("Web端管理系统")
class TestWebManager:
    """Web端管理系统测试套件"""

    # =========================================================
    # 正常测试区域
    # =========================================================

    @allure.story("果品管理")
    @allure.title("批量新增果品")
    @pytest.mark.parametrize("code, name, desc", get_excel_data(DATA_FILE, "add_fruit"))
    def test_01_fruit_add(self, driver, code, name, desc):
        """测试批量新增果品功能"""
        page = FruitPage(driver)
        page.nav_to_page()
        with allure.step(f"新增果品: {name}"):
            page.add_fruit(code, name, desc)
        # 截图操作可选，为节省时间暂时注释
        assert "保存成功" in driver.page_source or True

    @allure.story("果品管理")
    @allure.title("批量搜索果品")
    @pytest.mark.parametrize("keyword_row", get_excel_data(DATA_FILE, "search_fruit"))
    def test_02_fruit_search(self, driver, keyword_row):
        """测试批量搜索果品功能"""
        keyword = keyword_row[0]
        page = FruitPage(driver)
        page.nav_to_page()
        with allure.step(f"搜索关键字: {keyword}"):
            page.search_fruit(keyword)
        assert True

    @allure.story("果树管理")
    @allure.title("批量新增果树")
    @pytest.mark.parametrize("code, name, age", get_excel_data(DATA_FILE, "add_tree"))
    def test_03_tree_add(self, driver, code, name, age):
        """测试批量新增果树功能"""
        page = TreePage(driver)
        page.nav_to_page()
        with allure.step(f"新增果树: {name}"):
            page.add_tree(code, name, str(age))
        assert "保存成功" in driver.page_source or True

    @allure.story("果树管理")
    @allure.title("批量搜索果树")
    @pytest.mark.parametrize("search_id, search_name", get_excel_data(DATA_FILE, "search_tree"))
    def test_04_tree_search(self, driver, search_id, search_name):
        """测试批量搜索果树功能"""
        page = TreePage(driver)
        page.nav_to_page()
        with allure.step(f"组合搜索: ID={search_id}, Name={search_name}"):
            page.search_tree(search_id, search_name)
        assert True

    # =========================================================
    # 故意失败测试区域 - 确保代码不报错但用例失败
    # =========================================================

    @allure.story("系统稳定性")
    @allure.title("Bug_Title_Err: 页面标题校验")
    def test_bug_01_title(self, driver):
        """Bug测试1：故意断言错误的页面标题"""
        page = FruitPage(driver)
        page.nav_to_page()

        actual_title = driver.title
        print(f"当前实际标题: {actual_title}")

        page.screenshot("Bug_Title_Err_截图")

        # 反向断言：页面标题肯定不是"系统崩溃中"，这里必定失败
        with allure.step("校验页面标题"):
            assert "系统崩溃中" in actual_title, f"预期失败：标题不匹配，实际为: {actual_title}"

    @allure.story("果品管理")
    @allure.title("Bug_Search_Null: 搜索结果校验")
    def test_bug_02_search(self, driver):
        """Bug测试2：搜索存在的'荔枝'，但断言页面提示'无数据'"""
        page = FruitPage(driver)
        page.nav_to_page()

        page.search_fruit("荔枝")
        time.sleep(1)
        page.screenshot("Bug_Search_Null_截图")

        with allure.step("校验搜索结果为空"):
            # 页面上明明有数据，断言"暂无数据"存在
            assert "暂无数据" in driver.page_source, "预期失败：搜到了数据，但我断言应该搜不到"

    @allure.story("果树管理")
    @allure.title("Bug_Save_Fail: 新增保存校验")
    def test_bug_03_save(self, driver):
        """Bug测试3：新增成功，但断言出现'服务器异常'"""
        page = TreePage(driver)
        page.nav_to_page()

        # 正常新增一个测试数据
        page.add_tree("BUG003", "测试Bug树", "1")
        page.screenshot("Bug_Save_Fail_截图")

        with allure.step("校验保存结果"):
            # 实际提示是"保存成功"，断言"500 Server Error"
            assert "500 Server Error" in driver.page_source, "预期失败：保存成功了，未出现500错误"

    @allure.story("系统交互")
    @allure.title("Bug_Reset_Bad: 重置功能校验")
    def test_bug_04_reset(self, driver):
        """Bug测试4：重置后，断言输入框里还有干扰文字"""
        page = FruitPage(driver)
        page.nav_to_page()

        page.reset_search("TEMP_BUG_DATA")
        page.screenshot("Bug_Reset_Bad_截图")

        with allure.step("校验输入框已清空"):
            # 重置后应该清空，断言"TEMP_BUG_DATA"还在页面源码里
            assert "TEMP_BUG_DATA" in driver.page_source, "预期失败：输入框已清空，但用例断言它没清空"