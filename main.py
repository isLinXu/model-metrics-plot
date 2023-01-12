
from plots.metrics_plots import plot_metrics
from utils.dataloader import pd_read_csv

import argparse

def parse_opt(known=False):

    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Quick use model-metrics-plot")
    parser.add_argument('-c', '--csv', default='data/Pytorch_models_data.csv', help="csv path")
    parser.add_argument('-n', '--fig_name', default='plot_metrics.jpg', help="figure name")
    parser.add_argument('-t', '--title_name', default='MS COCO Object Detection', help="title_name")
    parser.add_argument('-x', '--xlabel_name', default='PyTorch FP16 RTX3080(ms/img)', help="xlabel_name")
    parser.add_argument('-y', '--ylabel_name', default='COCO Mask AP val', help="ylabel_name")
    parser.add_argument('-f', '--font_size', default=10, help="font_size")

    return parser.parse_known_args()[0] if known else parser.parse_args()



def main(opt):
    csv_path = opt.csv
    fig_name = opt.fig_name
    title_name = opt.title_name
    xlabel_name = opt.xlabel_name
    ylabel_name = opt.ylabel_name
    font_size = opt.font_size
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_name, title_name, xlabel_name, ylabel_name, font_size)


if __name__ == '__main__':
    opt = parse_opt()
    main(opt)
