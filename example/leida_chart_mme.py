import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import numpy as np

from utils.colors import colors_dark,colors_light,colors_classic,colors_common,colors_dark_private,colors_common_private,colors_hex
from utils.fonts import font_new_roman


def plot_evaluation_chart(csv_path, output_path='evaluation_chart_1116.png', font_size=25, figsize=(16, 16)):
    # 设置全局字体为Times New Roman
    rcParams['font.family'] = 'Times New Roman'

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
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)

    # 隐藏最外圈的圆
    ax.spines['polar'].set_visible(False)

    # 绘制每一行数据的多边形
    for i, row in enumerate(values):
        # cr = colors_dark[i]
        # cr = colors_light[i]
        # cr = colors_classic[i]
        # cr = colors_common[i]
        # cr = colors_dark_private[i]
        cr = colors_common_private[i]
        # cr = colors_3model[i]
        data = np.concatenate((row, [row[0]]))  # 闭合多边形
        label_name = model_labels[i]
        ax.fill(angles, data, alpha=0.25,color=cr)  # 填充多边形
        ax.plot(angles, data, label=label_name, linewidth=2.0,color=cr)  # 绘制多边形

        # 设置图例属性
        num_models = len(values)
        legend = ax.legend(bbox_to_anchor=(0.5, -0.15), loc='lower center', ncol=num_models, prop=font_new_roman)
        # legend = ax.legend(bbox_to_anchor=(0.5, -0.15), loc='lower center', ncol=, prop=font_new_roman )
        for line in legend.get_lines():
            line.set_linewidth(5)

    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # 显示并保存图形
    plt.show()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', transparent=True)


if __name__ == '__main__':
    # csv_path = '../data/mllm_acc_eval-csv1029.csv'
    # csv_path = '../data/mllm_acc_eval-csv1116.csv'
    # csv_path = '../data/csv/mllm_acc_eval-csv1110.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mllm_acc_eval-csv1117.csv'
    # output_path = 'evaluation_chart_1117.png'

    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mllm_acc_eval-csv1123.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval_FlanT5xxl_csv1125.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval_llama_csv1125.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval_vicuna_csv1125.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv1207.csv'
    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_private_1207.csv'
    # output_path = 'chart/evaluation_chart_private_1211.png'

    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval_3model_csv1217.csv'
    # output_path = 'chart/evaluation_chart_3model_1218.png'

    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_public_1217.csv'
    # output_path = 'chart/evaluation_chart_public_1217.png'

    # csv_path = '  /Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_private_1217.csv'
    # output_path = 'chart/evaluation_chart_private_1217.png'

    # csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_public_1211.csv'
    # output_path = 'chart/evaluation_chart_public_1211.png'
    # output_path = 'chart/evaluation_chart_vicuna_1125.png'

    csv_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/research/mllm_acc_eval-csv_private_1230.csv'
    output_path = 'chart/evaluation_chart_private_1230.png'


    plot_evaluation_chart(csv_path,output_path)
