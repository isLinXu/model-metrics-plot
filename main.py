from plots.bar_chart_plot import bar_chart_plot
from plots.line_metrics_plots import plot_metrics
from plots.mult_chart_plot import plot_chart
from plots.leida_chart_plot import plot_evaluation_chart
from utils.dataloader import pd_read_csv

import argparse


def parse_opt(known=False):
    parser = argparse.ArgumentParser(description="Quick use model-metrics-plot")
    parser.add_argument('-c', '--csv', default='data/Pytorch_models_data.csv', help="csv path")
    parser.add_argument('-n', '--fig_path', default='output/plot_metrics.jpg', help="figure path")
    parser.add_argument('-p', '--plot_type', default='line', help="i.e line, bar, scatter")
    parser.add_argument('-t', '--title_name', default='MS COCO Object Detection', help="title name")
    parser.add_argument('-x', '--xlabel_name', default='PyTorch FP16 RTX3080(ms/img)', help="xlabel name")
    parser.add_argument('-y', '--ylabel_name', default='COCO Mask AP val', help="ylabel name")
    parser.add_argument('-g', '--is_grid', default=False, help="is grid")
    parser.add_argument('-f', '--font_size', default=10, help="font_size")
    parser.add_argument('-v', '--value_type', default='mAP', help="value type,i.e mAP, FPS, ms")
    parser.add_argument('-r', '--colors', default='#0000FF', help="colors")

    return parser.parse_known_args()[0] if known else parser.parse_args()


def main(opt):
    csv_path = opt.csv
    fig_path = opt.fig_path
    plot_type = opt.plot_type
    title_name = opt.title_name
    xlabel_name = opt.xlabel_name
    ylabel_name = opt.ylabel_name
    is_grid = opt.is_grid
    font_size = opt.font_size
    value_type = opt.value_type
    colors = opt.colors

    # read data
    df = pd_read_csv(csv_path)
    # plot
    if plot_type == 'line':
        plot_metrics(df, fig_path, title_name, xlabel_name, ylabel_name, font_size, is_grid)
    elif plot_type == 'bar':
        bar_chart_plot(df, fig_path, value_type, title_name, xlabel_name, colors, is_grid)
    elif plot_type == 'chart':
        plot_chart(df, fig_path, is_grid, title_name, font_size)
    elif plot_type == 'leida':
        plot_evaluation_chart(csv_path, fig_path, font_size)

if __name__ == '__main__':
    opt = parse_opt()
    main(opt)
