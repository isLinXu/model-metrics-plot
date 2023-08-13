
import matplotlib.pyplot as plt
import pandas as pd

def scatter_plot(data_file, x_col, y_col):
    """
    绘制散点图

    Args:
        data_file: str, csv 文件路径
        x_col: str, 横坐标列名
        y_col: str, 纵坐标列名
    """
    # 读取 csv 文件
    df = pd.read_csv(data_file)

    # 获取数据
    x = df[x_col]
    y = df[y_col]

    # 绘制散点图
    plt.scatter(x, y)

    # 设置图表标题和横纵坐标标签
    plt.title('{} vs {}'.format(x_col, y_col))
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # 显示图表
    plt.show()

# 示例：绘制 'Average' vs 'Java' 的散点图
scatter_plot('../data/llm_code_eval.csv', 'Average', 'Java')