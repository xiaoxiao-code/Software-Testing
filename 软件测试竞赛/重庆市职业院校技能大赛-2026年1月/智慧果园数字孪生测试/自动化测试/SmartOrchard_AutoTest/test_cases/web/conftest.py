import pytest
from selenium import webdriver
from pages.web.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # 如需无头模式可取消注释
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.mufancloud.com/orchard/")

    # 初始化登录
    login = LoginPage(driver)
    login.login("administrator", "123456")
    login.enter_backend()

    yield driver
    driver.quit()