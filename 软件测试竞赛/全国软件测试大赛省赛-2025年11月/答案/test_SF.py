import os
import time
from datetime import datetime
import pytest
from cryptography.hazmat.primitives.asymmetric import ec
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


@pytest.fixture( scope="function" )
def driver():
    # 提交最终代码脚本时，请将驱动路径换回官方路径"C:\\Users\\86153\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    service = Service(
        executable_path="C:\\Users\\86153\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe" )
    driver = webdriver.Chrome( service=service )
    driver.get( "https://www.sf-express.com/" )
    driver.maximize_window()
    driver.implicitly_wait( 10 )
    yield driver
    driver.quit()


class TestSF:

    # test-code-start

    # 请在此处插入Selenium+Pytest代码
    @pytest.mark.parametrize("test_case_id,start_point,start_point2,end_point,end_point2", [
        ("001","黄埔区", "黄埔东苑","鼓楼区","南京大学"),
        ("002","鼓楼区","南京大学","黄埔区", "黄埔东苑"),
    ])
    def test_SF_R001(self,driver,test_case_id,start_point,start_point2,end_point,end_point2):
        test_method_name = "test_SF_R001"
        #点击【服务支持】
        driver.find_element(By.XPATH,'/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
        #点击【运费时效】
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[1]').click()
        # 点击始发地
        driver.find_element(By.XPATH,'//*[@id="origion"]/div/div/div[1]').click()
        driver.find_element(By.XPATH,'//*[@id="origincityPicker"]/div[2]/input').send_keys(start_point)
        driver.find_element(By.XPATH,'  // *[ @ id = "origincityPicker"] / div[2] / div[2] / ul / li[1]').click()
        # 始发地详细地址
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="origion"]/div/div/div[2]/figure/input').click()
        driver.find_element(By.XPATH, '//*[@id="origion"]/div/div/div[2]/figure/input').send_keys(start_point2)
        # 点击目的地
        driver.find_element(By.XPATH,'//*[@id="dests"]/div[1]/div/div[1]').click()
        driver.find_element(By.XPATH,'//*[@id="destsCityPicker"]/div[2]/input').send_keys(end_point)
        driver.find_element(By.XPATH,'//*[@id="destsCityPicker"]/div[2]/div[2]/ul/li').click()
        # 始发地详细地址
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="dests"]/div/div/div[2]/figure/input').click()
        driver.find_element(By.XPATH, '//*[@id="dests"]/div/div/div[2]/figure/input').send_keys(end_point2)
        # 重量输入框
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').click()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').clear()
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').send_keys(5)
        # 输入长宽高
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[1]/input').send_keys(20)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[2]/input').send_keys(15)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[3]/input').send_keys(25)
        # 选择日期
        driver.find_element(By.XPATH,'//*[@id="datetime"]/div/div[2]/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[3]/table[1]/tbody/tr[5]/td[1]/div/span').click()
        driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/button[2]').click()
        # 点击查询
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
        screenshot_name = f"{test_method_name}_{test_case_id}.png"
        self.take_screenshot(driver, screenshot_name)

    def test_SF_R002(self, driver):
        # 点击【服务支持】
        driver.find_element(By.XPATH, '/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
        # 点击【运费时效】
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[1]').click()
        # 点击始发地
        driver.find_element(By.XPATH, '//*[@id="origion"]/div/div/div[1]').click()
        # 点击港澳台
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[1]/ul/li[2]').click()
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[2]/span').click()
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[6]/span').click()
        #    点击目的地

        driver.find_element(By.XPATH, '//*[@id="dests"]/div[1]/div/div[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[8]/span').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[4]/span').click()
        # 重量输入框
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').click()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').clear()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').send_keys(5)
        # 输入长宽高
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[1]/input').send_keys(20)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[2]/input').send_keys(15)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[3]/input').send_keys(25)
        # 选择日期
        driver.find_element(By.XPATH, '//*[@id="datetime"]/div/div[2]/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/button[1]').click()
        # 点击查询
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
        test_method_name = "test_SF_R002"
        screenshot_name = f"{test_method_name}_001.png"
        self.take_screenshot(driver, screenshot_name)

    def test_SF_R003(self, driver):
            # 点击【服务支持】
            driver.find_element(By.XPATH, '/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
            # 点击【运费时效】
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
            driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[1]').click()
            # 点击始发地
            driver.find_element(By.XPATH, '//*[@id="origion"]/div/div/div[1]').click()
            # 点击港澳台
            driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[1]/ul/li[2]').click()
            driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[2]/span').click()
            driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[6]/span').click()
            #    点击目的地

            driver.find_element(By.XPATH, '//*[@id="dests"]/div[1]/div/div[1]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[8]/span').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[4]/span').click()
            # 重量输入框
            time.sleep(1)
            driver.find_element(By.XPATH,
                                '//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').click()
            driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').clear()
            driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').send_keys(100)
            # 选择日期
            driver.find_element(By.XPATH, '//*[@id="datetime"]/div/div[2]/input').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input').send_keys("2025-11-17")
            driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys("15:00:00")
            driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/button[2]').click()
            # 点击查询
            driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
            time.sleep(5)
            test_method_name = "test_SF_R003"
            screenshot_name = f"{test_method_name}_001.png"
            self.take_screenshot(driver, screenshot_name)

    @pytest.mark.parametrize("test_case_id,weight,length,width,height", [
        ("001", 1.5, 10, 20, 30),
        ("002", 5.0, 30, 40, 50),
        ("003", 10.0, 50, 60, 70),
        ("004", 25.0, 80, 90, 100)
    ])
    def test_SF_R004(self, driver, test_case_id, weight, length, width, height):
        test_method_name = "test_SF_R004"
        # 点击【服务支持】
        driver.find_element(By.XPATH, '/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
        # 点击【运费时效】
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[1]').click()
        # 点击始发地
        driver.find_element(By.XPATH, '//*[@id="origion"]/div/div/div[1]').click()
        # 点击港澳台
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[1]/ul/li[2]').click()
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[2]/span').click()
        driver.find_element(By.XPATH, '//*[@id="origincityPicker"]/div[3]/div[2]/ul/li[6]/span').click()
        #    点击目的地

        driver.find_element(By.XPATH, '//*[@id="dests"]/div[1]/div/div[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[8]/span').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="destsCityPicker"]/div[3]/div[2]/ul/li[4]/span').click()
        # 重量输入框
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').click()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').clear()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/figure/div/input').send_keys(weight)
        # 输入长宽高
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[1]/input').send_keys(length)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[2]/input').send_keys(width)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/figure/div/div[3]/input').send_keys(height)
        # 选择日期
        driver.find_element(By.XPATH, '//*[@id="datetime"]/div/div[2]/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input').send_keys("2025-11-18")
        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys("08:00:00")
        driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/button[2]').click()
        # 点击查询
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/button').click()
        # 点击【大件（20kg+）】按钮
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/ul[2]/li[2]').click()
        time.sleep(2)
        screenshot_name = f"{test_method_name}_{test_case_id}.png"
        self.take_screenshot(driver, screenshot_name)


    @pytest.mark.parametrize("elements", [
        ('//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/a[1]'),
        ('//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/a[2]/div[1]'),
        ('//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/a[3]/div[1]'),
        ('//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/a[4]/div[1]')
    ])
    def test_SF_R005(self, driver,elements):
        # 获取当前测试方法名
        test_method_name = "test_SF_R005"
        # 点击【服务支持】
        driver.find_element(By.XPATH, '/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
        # 点击【运费时效】
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[1]').click()
        # 依次点击
        driver.find_element(By.XPATH,elements).click()
        time.sleep(5)
        index = elements.split('/a[')[1].split(']')[0] if '/a[' in elements else '001'
        screenshot_name = f"{test_method_name}_{index.zfill(3)}.png"
        self.take_screenshot(driver, screenshot_name)

    def test_SF_R006(self,driver):
        driver.find_element(By.XPATH,"/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        # driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[1]/ul/li[3]/div').click()
        # time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[2]').click()
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/input').click()
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/div/div[3]/div[2]/ul/li[2]/span').click()
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/div/div[3]/div[2]/ul/li[1]/span').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="range-key-word"]').send_keys("兴业太古汇")
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/div[1]/span').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[2]/div/div[2]/div[1]/div[3]/button').click()
        time.sleep(10)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span[7]').click()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 750);")
        time.sleep(10)
        action = ActionChains(driver)
        slider = driver.find_element(By.XPATH,
                                     '//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[8]/div[2]/div[3]/div[4]')
        action.drag_and_drop_by_offset(slider, 0, 18).perform()  # 向下拖动18像素
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -350);")
        test_method_name = "test_SF_R006"
        screenshot_name = f"{test_method_name}_001.png"
        self.take_screenshot(driver, screenshot_name)

    @pytest.mark.parametrize("test_case_id,sjj,gjc", [
        ("001", "天河区", "正佳广场"),
        ("002", "福田区", "耀华楼"),
        ("003", "玄武区", "洪武北路"),
        ("004", "西湖区", "电信大楼"),
    ])
    def test_SF_R007(self,driver,test_case_id,sjj,gjc):
        test_method_name = "test_SF_R007"
        #点击【服务支持】
        driver.find_element(By.XPATH,'/html/body/div/section[1]/section/div/div[2]/div[4]/div[1]/a').click()
        #点击【服务网点】
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[1]/ul/li[3]/ul/li[2]').click()
        # 选择收寄件
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/div/div[2]/input').send_keys(sjj)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="range-query-citypicker"]/div/div[2]/div[2]/ul/li').click()
        time.sleep(1)
        # 输入关键词
        driver.find_element(By.XPATH,'//*[@id="range-key-word"]').send_keys(gjc)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="chn"]/div/div[2]/div/div[2]/div[1]/div[3]/button').click()
        action = ActionChains(driver)
        slider = driver.find_element(By.XPATH,
                                     '//*[@id="chn"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[8]/div[2]/div[3]/div[4]')
        action.drag_and_drop_by_offset(slider, 0, -50).perform()  # 向上拖动50像
        time.sleep(3)
        test_method_name = "test_SF_R007"
        screenshot_name = f"{test_method_name}_{test_case_id}.png"
        self.take_screenshot(driver, screenshot_name)
    # test-code-end
    @pytest.mark.parametrize(
        "test_case_id,item_input, item_select, case_id",
        [
            ("001","电子琴", "电子琴", "SF_R008_001"),
            ("002","笔记本电脑", "笔记本电脑", "SF_R008_002")
        ]
    )
    def test_SF_R008(self, driver,test_case_id,item_input, item_select, case_id):
        """
        执行 R008 需求：收寄标准查询（内地到内地）
        - SF_R008_001: 电子琴
        - SF_R008_002: 笔记本电脑
        """
        wait = WebDriverWait(driver, 10)

        # 1. 导航：首页 -> 服务支持 -> 收寄标准
        wait.until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(), '服务支持')]"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(text(), '收寄标准')]"))).click()

        time.sleep(1)

        # ---------------------------------
        # 2. 设置始发地: 广东省-深圳市-光明区
        # ---------------------------------
        el_origin = wait.until(
            ec.visibility_of_element_located((By.XPATH, "//input[@placeholder='请选择始发地国家/地区名称']")))
        el_origin.click()
        # 选择 '省/直辖市'
        driver.find_element(By.XPATH, '//*[@id="accept-from-input"]/div/div[3]/div[1]/ul/li[2]').click()
        # 选择省
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-from-input"]/div/div[3]/div[2]/ul/li[19]/span'))).click()
        # 选择市
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-from-input"]/div/div[3]/div[2]/ul/li[3]/span'))).click()
        # 选择区
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-from-input"]/div/div[3]/div[2]/ul/li[10]/span'))).click()

        time.sleep(1)
        # ---------------------------------
        # 3. 设置目的地: 江苏省-南京市-鼓楼区
        # ---------------------------------
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accept-to-input"]/input'))).click()
        # 选择 '省/直辖市'
        driver.find_element(By.XPATH, '//*[@id="accept-to-input"]/div/div[3]/div[1]/ul/li[2]').click()
        # 选择省
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-to-input"]/div/div[3]/div[2]/ul/li[10]/span'))).click()
        # 选择市
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-to-input"]/div/div[3]/div[2]/ul/li[1]/span'))).click()
        # 选择区
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="accept-to-input"]/div/div[3]/div[2]/ul/li[4]/span'))).click()

        # ---------------------------------
        # 4. 执行用例
        # ---------------------------------
        el_item = driver.find_element(By.XPATH, '//*[@id="accept-consignment-input"]/input')
        el_query_btn = driver.find_element(By.XPATH, '//*[@id="chn"]/div/div[2]/div/div[2]/button')

        el_item.clear()
        el_item.send_keys(item_input)

        select_xpath = f"//div[@class='cons-name']/span[text()='{item_select}']"
        wait.until(ec.element_to_be_clickable((By.XPATH, select_xpath))).click()

        el_query_btn.click()

        time.sleep(1)
        test_method_name = "test_SF_R008"
        screenshot_name = f"{test_method_name}_{test_case_id}.png"
        self.take_screenshot(driver, screenshot_name)

    @staticmethod
    def take_screenshot(driver, file_name):
        timestamp = datetime.now().strftime( "%H%M%S%d%f" )[:-3]
        timestamped_file_name = f"{timestamp}_{file_name}"
        screenshots_dir = "screenshots"
        if not os.path.exists( screenshots_dir ):
            os.makedirs( screenshots_dir )
        screenshot_file_path = os.path.join( screenshots_dir, timestamped_file_name )
        driver.save_screenshot( screenshot_file_path )
