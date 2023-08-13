
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
    plt.savefig('../output/{}_vs_{}.png'.format(x_col, y_col))
    # 显示图表
    plt.show()

def scatter_all_plot(data_file):
    """
    绘制散点图

    Args:
        data_file: str, csv 文件路径
    """
    # 读取 csv 文件
    df = pd.read_csv(data_file)

    # 获取列名
    cols = df.columns.tolist()

    # 绘制散点图
    for i in range(1, len(cols)):
        for j in range(i):
            x_col = cols[i]
            y_col = cols[j]
            x = df[x_col]
            y = df[y_col]
            plt.scatter(x, y)
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title('{} vs {}'.format(x_col, y_col))
            plt.savefig('../output/{}_vs_{}.png'.format(x_col, y_col))
            plt.show()



if __name__ == '__main__':
    # 示例：绘制 'Average' vs 'Java' 的散点图
    scatter_plot('../data/llm_code_eval.csv', 'Average', 'Java')

    # 示例：绘制所有列的散点图
    scatter_all_plot('../data/llm_code_eval.csv')