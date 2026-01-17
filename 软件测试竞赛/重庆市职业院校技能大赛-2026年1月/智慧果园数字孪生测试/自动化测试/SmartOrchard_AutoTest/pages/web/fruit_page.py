from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time

class FruitPage(BasePage):
    # 菜单
    LOC_MENU_BASE = (By.XPATH, "//span[text()='基础信息']")
    LOC_MENU_FRUIT = (By.XPATH, "//span[text()='果品类型']")

    # 新增/编辑弹窗
    LOC_ADD_BTN = (By.XPATH, "//button[.//span[text()='新增记录']]")
    LOC_INP_CODE = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[1]/div/div[1]/input')
    LOC_INP_NAME = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[2]/div/div[1]/input')
    LOC_INP_DESC = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[5]/div/div[2]/form/div[3]/div/div/input')
    LOC_SAVE_BTN = (By.XPATH, "//button[contains(., '确') and contains(., '定')]")

    # 搜索/重置
    LOC_SEARCH_INP = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[2]/div/div/div/input')
    LOC_SEARCH_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[3]/button[1]')
    LOC_RESET_BTN  = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[2]/form/div[3]/button[2]/span')

    # 表格操作 (第一行)
    LOC_COPY_BTN = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[3]/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/div/button[3]/span/div/span')
    LOC_DEL_BTN  = (By.XPATH, '//*[@id="app"]/div/main/section/div/div/div[2]/div[3]/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/div/button[2]')
    LOC_CONFIRM_DEL = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    def nav_to_page(self):
        self.driver.refresh()
        time.sleep(2)
        self.click(self.LOC_MENU_BASE)
        self.click(self.LOC_MENU_FRUIT)
        time.sleep(1)

    # 1. 新增
    def add_fruit(self, code, name, desc):
        self.click(self.LOC_ADD_BTN)
        self.send_keys(self.LOC_INP_CODE, code)
        self.send_keys(self.LOC_INP_NAME, name)
        self.send_keys(self.LOC_INP_DESC, desc)
        self.click(self.LOC_SAVE_BTN)
        time.sleep(1)

    # 2. 搜索
    def search_fruit(self, keyword):
        self.send_keys(self.LOC_SEARCH_INP, keyword)
        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)

    # 3. 触发校验 (只填名称，不填编号)
    def trigger_validation(self, name="验证测试"):
        self.click(self.LOC_ADD_BTN)
        self.send_keys(self.LOC_INP_NAME, name)
        self.click(self.LOC_SAVE_BTN)
        time.sleep(1)

    # 4. 重置搜索
    def reset_search(self, temp_data="TEMP_DATA"):
        self.send_keys(self.LOC_SEARCH_INP, temp_data)
        time.sleep(0.5)
        self.click(self.LOC_RESET_BTN)
        time.sleep(0.5)
        self.click(self.LOC_SEARCH_BTN)
        time.sleep(1)

    # 5. 复制并编辑
    def copy_and_edit(self, new_code):
        self.click(self.LOC_COPY_BTN)
        time.sleep(1)
        # 编辑弹窗出现，修改编号
        elem = self.find(self.LOC_INP_CODE)
        elem.clear()
        elem.send_keys(new_code)
        self.click(self.LOC_SAVE_BTN)
        time.sleep(1)

    # 6. 删除
    def delete_first_record(self):
        self.click(self.LOC_DEL_BTN)
        time.sleep(1)
        self.click(self.LOC_CONFIRM_DEL)
        time.sleep(1)