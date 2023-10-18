
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import numpy as np

from utils.colors import colors_dark

def plot_evaluation_chart(csv_path):
    # 设置全局字体为Times New Roman
    rcParams['font.family'] = 'Times New Roman'

    data_frame = pd.read_csv(csv_path)

    # 提取数据
    categories = list(data_frame.columns[1:])
    values = data_frame.values[:, 1:]
    model_labels = data_frame.values[:, 0]

    # 计算角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 闭合多边形

    fig, ax = plt.subplots(figsize=(16, 16), subplot_kw=dict(polar=True))

    # 设置坐标标签字体大小
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)

    colors = colors_dark

    font1 = {'family': 'Times New Roman',
             'weight': 'bold',
             'size': 18,
             }
    # 隐藏最外圈的圆
    ax.spines['polar'].set_visible(False)

    # 绘制每一行数据的多边形
    for i, row in enumerate(values):
        cr = colors[i]
        data = np.concatenate((row, [row[0]]))  # 闭合多边形
        label_name = model_labels[i]

        ax.fill(angles, data, alpha=0.25)  # 填充多边形
        ax.plot(angles, data, label=label_name, linewidth=2.0)  # 绘制多边形

        legend = ax.legend(bbox_to_anchor=(0.5, -0.15), loc='lower center', ncol=3, prop=font1)
        for line in legend.get_lines():
            line.set_linewidth(5)

    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # 显示图形
    plt.show()

    # 保存图形
    fig.savefig('evaluation-1013.png', dpi=300, bbox_inches='tight', transparent=True)

csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mllm_acc_eval-csv1013.csv'
plot_evaluation_chart(csv_path)