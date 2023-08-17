import random as random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from utils import pd_read_csv

def bar_chart(data_file, x_col, y_col):
    """
    绘制柱状图

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

    # 绘制柱状图
    plt.bar(x, y)

    # 设置图表标题和横纵坐标标签
    plt.title('{} vs {}'.format(x_col, y_col))
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # 显示图表
    plt.show()



def bar_chart_plot(df, fig_path, value_type='mAP', title_name="MS COCO Object Detection", xlabel_name="COCO mAP(%)",
                   color='#0000FF', is_grid=True):
    value_list = []
    name_list = []
    ms_list = []
    fps_list = []
    map_list = df['mAP']
    for i in range(0, len(map_list)):
        label = df[df['mAP'] == map_list[i]]['branch'].values
        ms = df[df['mAP'] == map_list[i]]['ms'].values
        fps = df[df['mAP'] == map_list[i]]['fps'].values
        model = df[df['mAP'] == map_list[i]]['model'].values
        # print('ms', ms, 'label', label, 'fps', fps, 'model', model)
        if map_list[i] != -1:
            name = model + label
            name_list.append(name)
        if value_type == 'mAP':
            value_list = map_list
        elif value_type == 'ms':
            value_list.append(float(ms))
        elif value_type == 'fps':
            value_list.append(float(fps))

    plt.barh(range(len(value_list)), value_list, height=0.5, color=color, alpha=0.8)  # 从下往上画
    plt.yticks(range(len(value_list)), name_list, size='small')
    plt.xlim(0, 100)
    plt.xlabel(xlabel_name)
    plt.title(title_name)
    for x, y in enumerate(value_list):
        plt.text(y + 0.2, x - 0.1, '%s' % y)

    # grid
    if is_grid:
        plt.grid()

    # save
    plt.savefig(fig_path, dpi=1080)

    # imshow
    plt.show()


if __name__ == '__main__':
    csv_path = '../data/MMYOLO_model_data.csv'
    fig_path = '../output/bar_chart_plot.jpg'
    value_type = 'mAP'
    df = pd_read_csv(csv_path)
    bar_chart_plot(df, fig_path, value_type)

    # 示例：绘制 'Metric' 列和 'Java' 列的柱状图
    bar_chart('../../data/llm_code_eval.csv', 'Metric', 'Java')
