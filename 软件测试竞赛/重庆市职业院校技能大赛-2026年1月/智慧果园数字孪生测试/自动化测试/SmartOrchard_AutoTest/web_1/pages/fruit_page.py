from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class FruitPage(BasePage):
    # 菜单定位
    LOC_MENU_BASE = (By.XPATH, "//span[text()='基础信息']")
    LOC_MENU_FRUIT = (By.XPATH, "//span[text()='果品类型']")

    # 按钮定位
    LOC_ADD_BTN = (By.XPATH, "//button[.//span[text()='新增记录']]")
    LOC_SAVE_BTN = (By.XPATH, "//button[contains(., '确') and contains(., '定')]")

    # 新增表单定位
    LOC_INP_CODE = (By.XPATH,
                    '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[1]/div/div[1]/input')
    LOC_INP_NAME = (By.XPATH,
                    '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[2]/div/div[1]/input')
    LOC_INP_DESC = (By.XPATH,
                    '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[3]/div/div/input')

    # 搜索定位
    LOC_SEARCH_INP = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[2]/div/div/div/input')
    LOC_SEARCH_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[3]/button[1]')

    def nav_to_page(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(self.LOC_MENU_BASE)
        self.click(self.LOC_MENU_FRUIT)
        time.sleep(1)

    def add_fruit(self, code, name, desc):
        self.click(self.LOC_ADD_BTN)
        self.send_keys(self.LOC_INP_CODE, code)
        self.send_keys(self.LOC_INP_NAME, name)
        self.send_keys(self.LOC_INP_DESC, desc)
        self.click(self.LOC_SAVE_BTN)
        time.sleep(1)

    def search_fruit(self, keyword):
        self.send_keys(self.LOC_SEARCH_INP, keyword)
        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)