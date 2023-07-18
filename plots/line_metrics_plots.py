import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

from utils.dataloader import pd_read_csv, fps_to_ms


def is_nan(x):
    return type(x) is float and math.isnan(float(x))


def plot_metrics(df, fig_path, title_name='MS COCO Object Detection',
                 xlabel_name='PyTorch FP16 RTX3080(ms/img)',
                 ylabel_name='COCO Mask AP val', font_size=10, is_grid=True):
    model_list = df['model'].unique()
    for i in range(0, len(model_list)):
        label_list = df[df['model'] == model_list[i]]['branch'].tolist()
        ms_list = df[df['model'] == model_list[i]]['ms'].values
        fps_list = df[df['model'] == model_list[i]]['fps'].values
        map_list = df[df['model'] == model_list[i]]['mAP'].values
        maker_list = df[df['model'] == model_list[i]]['maker'].values

        y_list = map_list
        t_list = []

        if fps_list[0] == -1:
            x_list = ms_list
        else:
            for j in fps_list:
                j = fps_to_ms(j)
                t_list.append(j)
            x_list = t_list

        plt.plot(x_list, y_list, marker=maker_list[0], markersize=font_size)

        plt.title(title_name)
        plt.xlabel(xlabel_name)
        plt.ylabel(ylabel_name)

        for ms, map, label in zip(x_list, y_list, label_list):
            plt.text(ms, map, label, ha='center', va='bottom', fontsize=font_size)

    # grid
    if is_grid:
        plt.grid()
    # legend
    plt.legend(model_list, loc='lower right')
    # save
    plt.savefig(fig_path, dpi=1080)
    # show
    plt.show()


def plot_multiple_line_charts(data, x_column, y_columns, xlabel, ylabel, title, save_fig='result.png'):
    # 提取x轴数据
    x_data = data[x_column]

    # 绘制多条折线
    for y_column in y_columns:
        y_data = data[y_column]
        plt.plot(x_data, y_data, label=y_column, marker='o')

    # 为x轴和y轴添加标签
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # 为图形添加标题
    plt.title(title)

    # 添加图例
    plt.legend()
    plt.savefig(save_fig, dpi=1080)
    # 显示图形
    plt.show()


if __name__ == '__main__':
    csv_path = '../data/Pytorch_models_data.csv'
    fig_path = 'plot_metrics.jpg'
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_path)

    # 读取CSV文件
    csv_path = "../data/result_cora.csv"
    data = pd_read_csv(csv_path)

    # 调用函数绘制多条折线图
    plot_multiple_line_charts(data, "LR(%)", ["Random", "HyperNAS-RL", "HyperNAS"], "LR(%)", "Accuracy", "Cora")
