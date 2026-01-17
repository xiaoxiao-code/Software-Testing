from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time


class LoginPage(BasePage):
    # 严格保持 Test_02.py 中的定位
    LOC_SKIP = (By.XPATH, '//*[@id="app"]/div/div')
    LOC_USER = (By.XPATH, '//*[@id="pane-first"]/form/div[1]/div/div/input')
    LOC_PWD = (By.XPATH, '//*[@id="pane-first"]/form/div[2]/div/div/input')
    LOC_CODE = (By.XPATH, '//*[@id="pane-first"]/form/div[3]/div/div/div[1]/div/input')
    LOC_BTN = (By.XPATH, '//*[@id="pane-first"]/form/div[5]/div/button')

    # 菜单定位
    LOC_HEADER_USER = (By.XPATH, '//*[@id="app"]/div/header/div[3]/div[2]/div/span')
    LOC_ADMIN_LINK = (By.XPATH, "//a[contains(text(), '后台管理')]")

    def login(self, user, pwd):
        time.sleep(1)
        # 跳过动画逻辑
        try:
            self.click(self.LOC_SKIP)
        except:
            print("跳过动画失败或无需跳过")

        self.send_keys(self.LOC_USER, user)
        self.send_keys(self.LOC_PWD, pwd)
        self.click(self.LOC_CODE)

        # 你的逻辑是等待10秒手动输入验证码
        time.sleep(10)

        self.click(self.LOC_BTN)
        time.sleep(3)

    def enter_backend(self):
        self.click(self.LOC_HEADER_USER)
        time.sleep(1)
        self.click(self.LOC_ADMIN_LINK)
        time.sleep(2)
        # 切换句柄
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])