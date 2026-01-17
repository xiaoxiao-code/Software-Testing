# run_tests.py - 测试运行主入口，支持多模块独立运行和报告生成
import pytest
import os
import sys
import shutil

MODULE = "unity"

def main():
    """主函数：执行测试运行流程"""
    # 获取项目根目录并添加到系统路径
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE)

    # Allure工具路径配置
    ALLURE_BIN = r"D:\allure-2.36.0\allure-commandline-2.36.0\allure-2.36.0\bin"
    os.environ["PATH"] = ALLURE_BIN + os.pathsep + os.environ["PATH"]

    # 构建测试相关路径
    test_dir = os.path.join(BASE, "test_cases", MODULE)  # 测试用例目录
    xml_path = os.path.join(BASE, "report", MODULE, "xml")  # 报告数据目录
    html_path = os.path.join(BASE, "report", MODULE, "html")  # 报告展示目录

    # 检查测试目录是否存在
    if not os.path.exists(test_dir):
        print(f"找不到测试目录: {test_dir}")
        return

    # 清理旧报告数据
    if os.path.exists(xml_path):
        shutil.rmtree(xml_path, ignore_errors=True)

    # 运行测试
    print(f"正在运行 [{MODULE}] 模块测试...")
    pytest.main(["-vs", test_dir, f"--alluredir={xml_path}", "--clean-alluredir"])

    # 生成HTML报告
    if shutil.which("allure") and os.path.exists(xml_path) and os.listdir(xml_path):
        os.system(f"allure generate {xml_path} -o {html_path} --clean")
        print(f"报告生成成功！正在打开...")
        os.system(f"allure open {html_path}")
    else:
        print("未生成测试数据或Allure未正确配置。")


# if __name__ == "__main__":
#     main()
