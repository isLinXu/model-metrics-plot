from plots.metrics_plots import plot_metrics
from utils.dataloader import pd_read_csv

if __name__ == '__main__':
    csv_path = '/home/linxu/PycharmProjects/model-metrics-plot/data/yolo_model_data.csv'
    fig_name = 'plot_metrics.jpg'
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_name)