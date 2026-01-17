# -*- encoding=utf8 -*-
import pytest
import os

# ================= 配置区 =================
ALLURE_BIN_PATH = r"D:\allure-2.36.0\allure-commandline-2.36.0\allure-2.36.0\bin"
REPORT_ROOT = r"./report/report_01"
RAW_DATA_DIR = os.path.join(REPORT_ROOT, "json")
HTML_REPORT_DIR = os.path.join(REPORT_ROOT, "html")

if __name__ == "__main__":
    if ALLURE_BIN_PATH not in os.environ["PATH"]:
        os.environ["PATH"] = ALLURE_BIN_PATH
    pytest.main(["./test_cases","-s","-v",f"--alluredir={RAW_DATA_DIR}"])
    os.system(f"allure generate {RAW_DATA_DIR} -o {HTML_REPORT_DIR} --clean")





