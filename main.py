
from plots.metrics_plots import plot_metrics
from utils.dataloader import pd_read_csv

import argparse

parser = argparse.ArgumentParser(description="Quick use model-metrics-plot")
parser.add_argument('-c', '--csv', default='data/yolo_models_data.csv', help="csv path")
parser.add_argument('-n', '--name',default='plot_metrics.jpg', help="figure name")
argparse = parser.parse_args()


if __name__ == '__main__':
    csv_path = 'data/yolo_models_data.csv'
    fig_name = 'plot_metrics.jpg'
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_name)