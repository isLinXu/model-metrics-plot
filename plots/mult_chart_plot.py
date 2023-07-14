
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from utils.dataloader import pd_read_csv

def plot_chart(df,fig_path,is_grid,title_name,font_size):
    # 提取数据
    categories = list(df.columns[1:])
    values = df.values[:, 1:]
    model_labels = df.values[:, 0]

    # 计算角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 闭合多边形

    fig, ax = plt.subplots(figsize=(16, 16), subplot_kw=dict(polar=True))

    # 设置坐标标签字体大小
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    if is_grid is False:
        # 隐藏最外圈的圆
        ax.spines['polar'].set_visible(False)
        # 隐藏圆形网格线
        ax.grid(False)

    # 绘制每一行数据的多边形
    for i, row in enumerate(values):
        data = np.concatenate((row, [row[0]]))  # 闭合多边形
        label_name = model_labels[i]

        ax.plot(angles, data, label=label_name)  # 绘制多边形
        # ax.legend(label_name, fontsize=18)
        ax.fill(angles, data, alpha=0.25)  # 填充多边形
        # 添加图例并设置位置
        # ax.legend(bbox_to_anchor=(1, 0), loc='lower right')

    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    # plt.legend(loc="lower left")

    ax.set_xticklabels(categories)
    ax.set_title(title_name, fontsize=font_size)

    # 添加图例
    ax.legend(bbox_to_anchor=(1.0, 1.1))

    # 显示图形
    plt.show()

    # 保存图形
    fig.savefig(fig_path, dpi=300, bbox_inches='tight', transparent=True)

if __name__ == '__main__':
    csv_path = '../data/llm_code_eval.csv'
    fig_path = '../img/plot_mult_code_chart.jpg'
    is_grid = False
    title_name = 'LLM Eval'
    plot_type = 'chart'
    font_size = 18
    df = pd_read_csv(csv_path)
    plot_chart(df, fig_path, is_grid, title_name, font_size)
