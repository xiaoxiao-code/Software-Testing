from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LoginPage(BasePage):
    LOC_SKIP = (By.XPATH, '//*[@id="app"]/div/div')
    LOC_USER = (By.XPATH, '//*[@id="pane-first"]/form/div[1]/div/div/input')
    LOC_PWD = (By.XPATH, '//*[@id="pane-first"]/form/div[2]/div/div/input')
    LOC_CODE = (By.XPATH, '//*[@id="pane-first"]/form/div[3]/div/div/div[1]/div/input')
    LOC_BTN = (By.XPATH, '//*[@id="pane-first"]/form/div[5]/div/button')

    LOC_HEADER_USER = (By.XPATH, '//*[@id="app"]/div/header/div[3]/div[2]/div/span')
    LOC_ADMIN_LINK = (By.XPATH, "//a[contains(text(), '后台管理')]")

    def login_flow(self, user, pwd):
        time.sleep(1)
        # 尝试跳过动画
        try:
            self.click(self.LOC_SKIP)
        except:
            print("无需跳过动画")

        time.sleep(2)
        self.send_keys(self.LOC_USER, user)
        self.send_keys(self.LOC_PWD, pwd)

        # 点击验证码输入框，留出时间手动输入
        self.click(self.LOC_CODE)
        print(">>> 请手动输入验证码 (10秒等待)...")
        time.sleep(10)

        # 登录
        self.click(self.LOC_BTN)
        time.sleep(3)

        # 进入后台
        self.click(self.LOC_HEADER_USER)
        time.sleep(1)
        self.click(self.LOC_ADMIN_LINK)
        time.sleep(2)

        # 切换到新窗口
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        print(f"登录成功，当前页面: {self.driver.title}")