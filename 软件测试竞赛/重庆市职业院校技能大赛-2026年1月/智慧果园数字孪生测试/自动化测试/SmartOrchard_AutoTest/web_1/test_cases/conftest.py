import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 关键：将 web_1 目录加入系统路径，这样才能导入 pages 包
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def driver():
    """启动浏览器"""
    service = Service()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # 需要无头模式时取消注释
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.mufancloud.com/orchard/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="class", autouse=True)
def login_setup(driver):
    """自动登录"""
    login_page = LoginPage(driver)
    login_page.login_flow("administrator", "123456")