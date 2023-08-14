import matplotlib.pyplot as plt
import pandas as pd

def pie_chart(data_file, label_col, value_col):
    """
    绘制饼图

    Args:
        data_file: str, csv 文件路径
        label_col: str, 标签列名
        value_col: str, 值列名
    """
    # 读取 csv 文件
    df = pd.read_csv(data_file)

    # 获取数据
    labels = df[label_col]
    values = df[value_col]

    # 绘制饼图
    plt.pie(values, labels=labels, autopct='%1.1f%%')

    # 设置图表标题
    plt.title('{} vs {}'.format(label_col, value_col))

    # 显示图表
    plt.show()



if __name__ == '__main__':
    # 示例：绘制 'Metric' 列和 'Java' 列的饼图
    pie_chart('/Users/gatilin/PycharmProjects/model-metrics-plot/data/llm_code_eval.csv', 'Metric', 'Java')