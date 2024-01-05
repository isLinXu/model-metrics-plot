import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from adjustText import adjust_text

from utils.colors import colors_dark, colors_light, colors_classic, colors_common, colors_dark_private, \
    colors_common_private, colors_hex
from utils.fonts import font_new_roman

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from adjustText import adjust_text


def plot_evaluation_chart(csv_path, output_path='evaluation_chart.png', figsize=(16, 16), style=None):
    if style is None:
        style = {
            'font_family': 'Times New Roman',
            'font_size': 25,
            'legend_font_size': 20,
            'colors': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                       '#bcbd22', '#17becf',
                       'darkblue', 'darkorange', 'darkgreen', 'darkred', 'darkviolet', 'saddlebrown', 'deeppink',
                       'dimgray', 'darkolivegreen', 'darkcyan']
        }

    # 设置全局字体
    plt.rcParams['font.family'] = style['font_family']

    # 读取CSV文件并提取数据
    data_frame = pd.read_csv(csv_path)
    categories = list(data_frame.columns[1:])
    values = data_frame.values[:, 1:]
    model_labels = data_frame.values[:, 0]

    # 计算角度并闭合多边形
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    # 创建极坐标图并设置大小
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))

    # 设置坐标标签字体大小
    plt.xticks(fontsize=style['font_size'])
    plt.yticks(fontsize=style['font_size'])

    # 隐藏最外圈的圆
    ax.spines['polar'].set_visible(False)

    # 绘制每一行数据的多边形
    texts = []
    for i, row in enumerate(values):
        cr = style['colors'][i % len(style['colors'])]
        data = np.concatenate((row, [row[0]]))  # 闭合多边形
        label_name = model_labels[i]
        ax.fill(angles, data, alpha=0.25, color=cr)  # 填充多边形
        ax.plot(angles, data, label=label_name, linewidth=2.0, color=cr)  # 绘制多边形

        # 添加数据点上的文本
        for j, value in enumerate(row):
            angle_rad = angles[j]
            if angle_rad == 0:
                ha, distance = 'center', 10
            elif 0 < angle_rad < np.pi:
                ha, distance = 'left', 1
            elif angle_rad == np.pi:
                ha, distance = 'center', 10
            else:
                ha, distance = 'right', 1
            text = ax.text(angle_rad, value + distance, f'{value:.2f}', size=style['font_size'], color=cr,
                           horizontalalignment=ha)
            texts.append(text)

    # 调整文本位置以避免重叠
    adjust_text(texts, expand_text=(1.05, 1.2), expand_points=(1.05, 1.2), force_text=(0.1, 0.25),
                force_points=(0.2, 0.5), ax=ax)

    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # 设置图例属性
    num_models = len(values)
    legend = ax.legend(bbox_to_anchor=(0.5, -0.15), loc='lower center', ncol=num_models,
                       prop={'size': style['legend_font_size']})
    for line in legend.get_lines():
        line.set_linewidth(5)

    # 显示并保存图形
    plt.show()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)


if __name__ == '__main__':
    csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_private_1230.csv'
    output_path = 'chart/evaluation_chart_private_1230.png'
    plot_evaluation_chart(csv_path, output_path)
