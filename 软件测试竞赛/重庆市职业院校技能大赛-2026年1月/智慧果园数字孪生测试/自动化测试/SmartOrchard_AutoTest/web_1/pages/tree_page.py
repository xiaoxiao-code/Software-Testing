from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class TreePage(BasePage):
    LOC_MENU_BASE = (By.XPATH, "//span[text()='基础信息']")
    LOC_MENU_TREE = (By.XPATH, "//span[text()='果树信息']")

    LOC_ADD_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[1]/button/span/span')
    LOC_SAVE_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[3]/div/button[2]')

    # 新增表单
    LOC_INP_CODE = (By.XPATH,
                    '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[1]/div/div[1]/input')
    LOC_INP_NAME = (By.XPATH,
                    '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[2]/div/div[1]/input')

    # 日期与来源选择
    LOC_DATE_INP = (By.XPATH, "//input[@placeholder='选择种植日期']")
    LOC_DATE_SEL = (By.XPATH, "//td[contains(@class, 'available')]//span[contains(text(), '12')]")
    LOC_SRC_INP = (By.XPATH,
                   '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[6]/div/div[1]/div/input')
    LOC_SRC_OPT = (By.XPATH, "//li[contains(@class, 'el-select-dropdown__item')]//span[text()='幼苗采购']")

    LOC_INP_AGE = (By.XPATH,
                   '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[5]/div/div/div/input')

    # 搜索定位
    LOC_SEARCH_ID = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[1]/div/div/div/input')
    LOC_SEARCH_NAME = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[2]/div/div/div/input')
    LOC_SEARCH_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[4]/button[1]')

    def nav_to_page(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(self.LOC_MENU_BASE)
        self.click(self.LOC_MENU_TREE)
        time.sleep(1)

    def add_tree(self, code, name, age):
        self.click(self.LOC_ADD_BTN)
        time.sleep(1)
        self.send_keys(self.LOC_INP_CODE, code)
        self.send_keys(self.LOC_INP_NAME, name)

        # 日期选择逻辑
        self.click(self.LOC_DATE_INP)
        time.sleep(1)
        self.click(self.LOC_DATE_SEL)

        # 来源选择逻辑
        self.click(self.LOC_SRC_INP)
        time.sleep(1)
        self.click(self.LOC_SRC_OPT)

        self.send_keys(self.LOC_INP_AGE, age)
        self.click(self.LOC_SAVE_BTN)
        time.sleep(1)

    def search_tree(self, search_id, search_name):
        if search_id:
            self.send_keys(self.LOC_SEARCH_ID, search_id)
        if search_name:
            self.send_keys(self.LOC_SEARCH_NAME, search_name)

        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)