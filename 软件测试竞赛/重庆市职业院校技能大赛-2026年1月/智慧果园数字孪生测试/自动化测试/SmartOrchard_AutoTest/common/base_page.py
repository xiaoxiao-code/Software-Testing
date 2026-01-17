from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import allure
import os
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(str(text)) # 强制转str，防止数字报错

    def screenshot(self, name):
        """截图并挂载到Allure报告"""
        timestamp = datetime.now().strftime("%H%M%S%f")[:-3]
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f"{timestamp}_{name}",
                      attachment_type=allure.attachment_type.PNG)