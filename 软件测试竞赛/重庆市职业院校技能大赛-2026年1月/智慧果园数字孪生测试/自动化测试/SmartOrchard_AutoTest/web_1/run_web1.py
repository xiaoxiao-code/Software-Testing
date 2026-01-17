# run_allure_tests.py - 测试运行和Allure报告生成脚本
import os
import pytest
import shutil
import time

# 1. 配置Allure命令行工具路径
# 注意：请确认此路径下包含'allure.bat'文件
ALLURE_BIN_PATH = r"D:\allure-2.36.0\allure-commandline-2.36.0\allure-2.36.0\bin"

# 2. 将Allure路径临时添加到系统环境变量PATH中
# 这一步是解决命令未找到问题的关键
if ALLURE_BIN_PATH not in os.environ["PATH"]:
    os.environ["PATH"] = ALLURE_BIN_PATH + os.pathsep + os.environ["PATH"]

# 定义测试结果和报告的存放路径
KEYWORD = "web1"  # 测试用例标记，可根据需要修改
RAW_RESULT_DIR = './result'  # 存放JSON/XML中间结果
HTML_REPORT_DIR = './report'  # 存放生成的HTML网页报告

def run_tests():
    """主函数：执行测试并生成报告"""

    # 第一步：清理旧文件（可选，推荐清理以避免历史数据干扰）
    if os.path.exists(RAW_RESULT_DIR):
        shutil.rmtree(RAW_RESULT_DIR)
    if os.path.exists(HTML_REPORT_DIR):
        shutil.rmtree(HTML_REPORT_DIR)

    # 第二步：使用pytest运行测试
    # -vs: 显示详细信息
    # --alluredir: 指定生成中间数据的目录
    # ./testcases: 测试用例目录，根据实际情况修改
    pytest_args = [
        '-vs',
        './test_cases',  # 替换为实际的测试脚本目录
        '--alluredir', RAW_RESULT_DIR,
        '--clean-alluredir'
    ]

    print("正在执行测试用例...")
    pytest.main(pytest_args)

    # 第三步：生成Allure HTML报告
    print("正在生成测试报告...")

    # 使用os.system调用命令行生成报告
    # generate: 生成命令
    # RAW_RESULT_DIR: 源数据目录
    # -o HTML_REPORT_DIR: 输出目录
    # --clean: 清除输出目录中的旧数据
    generate_cmd = f"allure generate {RAW_RESULT_DIR} -o {HTML_REPORT_DIR} --clean"

    try:
        exit_code = os.system(generate_cmd)
        if exit_code != 0:
            print("报告生成失败！可能是路径配置错误。")
            print(f"当前尝试使用的路径是: {ALLURE_BIN_PATH}")
        else:
            print(f"报告生成成功！位置: {os.path.abspath(HTML_REPORT_DIR)}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == '__main__':
    """脚本主入口"""
    run_tests()