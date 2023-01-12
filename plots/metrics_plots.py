import math
import matplotlib.pyplot as plt

from utils.dataloader import pd_read_csv, fps_to_ms


def is_nan(x):
    return type(x) is float and math.isnan(float(x))


def plot_metrics(df, fig_name, title_name='MS COCO Object Detection',
                 xlabel_name='PyTorch FP16 RTX3080(ms/img)',
                 ylabel_name='COCO Mask AP val', font_size=10):

    model_list = df['model'].unique()

    for i in range(0, len(model_list)):
        label_list = df[df['model'] == model_list[i]]['branch'].tolist()
        ms_list = df[df['model'] == model_list[i]]['ms'].values
        fps_list = df[df['model'] == model_list[i]]['fps'].values
        map_list = df[df['model'] == model_list[i]]['mAP'].values

        y_list = map_list
        t_list = []

        if fps_list[0] == -1:
            x_list = ms_list
        else:
            for j in fps_list:
                j = fps_to_ms(j)
                t_list.append(j)
            x_list = t_list

        plt.plot(x_list, y_list, marker='.', markersize=10)
        plt.title(title_name)
        plt.xlabel(xlabel_name)
        plt.ylabel(ylabel_name)
        for ms, map, label in zip(x_list, y_list, label_list):
            plt.text(ms, map, label, ha='center', va='bottom', fontsize=font_size)
    # legend
    plt.legend(model_list, loc='lower right')

    # save
    plt.savefig(fig_name, dpi=640)
    # show
    plt.show()


if __name__ == '__main__':
    csv_path = '/home/linxu/PycharmProjects/model-metrics-plot/data/Pytorch_models_data.csv'
    fig_name = 'plot_metrics.jpg'
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_name)
