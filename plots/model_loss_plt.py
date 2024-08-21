import json
import matplotlib.pyplot as plt

def plot_loss_curve(file_path):
    # 读取文件内容
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # 将单引号替换为双引号并解析内容
    data = [json.loads(line.replace("'", '"')) for line in lines]

    # 提取epoch和loss数据
    epochs = [d['epoch'] for d in data]
    losses = [d['loss'] for d in data]

    # 绘制曲线
    plt.plot(epochs, losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss Curve')
    plt.show()

# 调用函数
file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mgm_2b_loss.txt'
plot_loss_curve(file_path)