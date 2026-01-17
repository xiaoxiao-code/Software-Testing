from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time


class TreePage(BasePage):
    LOC_MENU_BASE = (By.XPATH, "//span[text()='基础信息']")
    LOC_MENU_TREE = (By.XPATH, "//span[text()='果树信息']")

    # 新增相关
    LOC_ADD_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[1]/button/span/span')
    LOC_CODE = (By.XPATH,
                '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[1]/div/div[1]/input')
    LOC_NAME = (By.XPATH,
                '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[2]/div/div[1]/input')

    # 日期和来源（特殊处理）
    LOC_DATE_INP = (By.XPATH, "//input[@placeholder='选择种植日期']")
    LOC_DATE_SEL = (By.XPATH, "//td[contains(@class, 'available')]//span[contains(text(), '12')]")
    # 注意：这里修正一下日期输入框定位，用于校验测试
    LOC_DATE_FORM_ITEM = (By.XPATH,
                          '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[4]/div/div[1]/input')

    LOC_SRC_INP = (By.XPATH,
                   '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[6]/div/div[1]/div/input')
    LOC_SRC_OPT = (By.XPATH, "//li[contains(@class, 'el-select-dropdown__item')]//span[text()='幼苗采购']")

    LOC_AGE = (By.XPATH,
               '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[5]/div/div/div/input')
    LOC_SAVE = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[3]/div/button[2]')

    # 搜索相关
    LOC_SEARCH_ID = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[1]/div/div/div/input')
    LOC_SEARCH_NAME = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[2]/div/div/div/input')
    LOC_SEARCH_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[4]/button[1]')
    LOC_RESET_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[4]/button[2]/span')

    def nav_to_page(self):
        self.driver.refresh()
        time.sleep(3)  # 等待页面刷新加载

        self.click(self.LOC_MENU_BASE)
        time.sleep(1)  # 等待动画
        self.click(self.LOC_MENU_TREE)
        time.sleep(1)

    # 1. 新增
    def add_tree(self, code, name, age):
        self.click(self.LOC_ADD_BTN)
        time.sleep(1)
        self.send_keys(self.LOC_CODE, code)
        self.send_keys(self.LOC_NAME, name)

        self.click(self.LOC_DATE_INP)
        time.sleep(1)
        self.click(self.LOC_DATE_SEL)

        self.click(self.LOC_SRC_INP)
        time.sleep(1)
        self.click(self.LOC_SRC_OPT)

        self.send_keys(self.LOC_AGE, age)
        self.click(self.LOC_SAVE)
        time.sleep(1)

    # 2. 搜索
    def search_tree(self, tree_id, tree_name):
        if tree_id:
            self.send_keys(self.LOC_SEARCH_ID, tree_id)
        if tree_name:
            self.send_keys(self.LOC_SEARCH_NAME, tree_name)
        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)

    # 3. 触发校验
    def trigger_validation(self):
        self.click(self.LOC_ADD_BTN)
        time.sleep(1)
        # 点击日期框但不选，直接保存
        self.click(self.LOC_DATE_FORM_ITEM)
        time.sleep(1)
        self.click(self.LOC_DATE_SEL)
        self.click(self.LOC_SAVE)
        time.sleep(1)

    # 4. 重置搜索
    def reset_search(self, temp_data="TEMP_DATA"):
        self.send_keys(self.LOC_SEARCH_ID, temp_data)
        time.sleep(0.5)
        self.click(self.LOC_RESET_BTN)
        time.sleep(0.5)
        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)