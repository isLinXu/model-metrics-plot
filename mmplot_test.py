from mmplot.plots import plot_metrics
from mmplot.utils.dataloader import pd_read_csv

if __name__ == '__main__':
    csv_path = 'data/Pytorch_models_data.csv'
    fig_name = 'plot_metrics.jpg'
    df = pd_read_csv(csv_path)
    plot_metrics(df, fig_name)
    plot_metrics()