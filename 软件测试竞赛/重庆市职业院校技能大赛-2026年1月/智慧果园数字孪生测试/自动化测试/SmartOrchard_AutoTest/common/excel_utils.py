import pandas as pd
import os

def get_excel_data(file_path, sheet_name):
    """
    读取Excel数据，将空值处理为空字符串，返回列表嵌套元组
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel文件未找到: {file_path}")

    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)

    return [tuple(x) for x in df.values]

