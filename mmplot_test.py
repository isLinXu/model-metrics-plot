
from mmplot.core.run import plots
import mmplot.utils


import argparse
def parse_opt(known=False):

    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Quick use model-metrics-plot")
    parser.add_argument('-c', '--csv', default='data/PaddleYOLO_model_data.csv', help="csv path")
    parser.add_argument('-n', '--fig_name', default='plot_metrics.jpg', help="figure name")
    parser.add_argument('-t', '--title_name', default='MS COCO Object Detection', help="title_name")
    parser.add_argument('-x', '--xlabel_name', default='PyTorch FP16 RTX3080(ms/img)', help="xlabel_name")
    parser.add_argument('-y', '--ylabel_name', default='COCO Mask AP val', help="ylabel_name")
    parser.add_argument('-f', '--font_size', default=10, help="font_size")

    return parser.parse_known_args()[0] if known else parser.parse_args()


if __name__ == '__main__':
    # run()
    opt = parse_opt()
    plots(opt)