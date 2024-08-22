import json
import matplotlib.pyplot as plt
import re

def plot_loss_curve(file_path):
    # 读取文件内容
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # 使用正则表达式匹配包含'loss'的行并捕获数据
    pattern = re.compile(r"\'loss\':\s*(\d+\.\d+),\s*\'grad_norm\':\s*\d+\.\d+,\s*\'learning_rate\':\s*\d+\.\d+,\s*\'epoch\':\s*(\d+\.\d+)")
    data = [match.groups() for line in lines for match in [pattern.search(line)] if match]

    # 转换数据为浮点数并提取epoch和loss数据
    epochs = [float(d[1]) for d in data]
    losses = [float(d[0]) for d in data]

    # 绘制曲线
    plt.plot(epochs, losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss Curve')

    # 找到最低点并绘制垂直线
    min_index = losses.index(min(losses))
    min_epoch = epochs[min_index]
    min_loss = losses[min_index]
    plt.axvline(x=min_epoch, color='r', linestyle='--')

    # 绘制水平线并在该线上显示损失值
    plt.axhline(y=min_loss, color='r', linestyle='--')
    plt.text(min_epoch, min_loss, f'Min Loss: {min_loss:.4f}', va='bottom', ha='left')

    plt.show()


def plot_mult_loss_curve(file_paths):
    # all_epochs = []
    # all_losses = []
    # num_epochs_per_stage = []
    #
    # for file_path in file_paths:
    #     # 读取文件内容
    #     with open(file_path, 'r') as f:
    #         lines = f.readlines()
    #
    #     # 使用正则表达式匹配包含'loss'的行并捕获数据
    #     pattern = re.compile(r"\'loss\':\s*(\d+\.\d+),\s*\'grad_norm\':\s*\d+\.\d+,\s*\'learning_rate\':\s*\d+\.\d+,\s*\'epoch\':\s*(\d+\.\d+)")
    #     data = [match.groups() for line in lines for match in [pattern.search(line)] if match]
    #
    #     # 转换数据为浮点数并提取epoch和loss数据
    #     epochs = [float(d[1]) for d in data]
    #     losses = [float(d[0]) for d in data]
    #
    #     # 如果不是第一个阶段，将横轴偏移
    #     if all_epochs:
    #         epoch_offset = all_epochs[-1]
    #         epochs = [epoch + epoch_offset for epoch in epochs]
    #
    #     # 将当前阶段的数据添加到总数据中
    #     all_epochs.extend(epochs)
    #     all_losses.extend(losses)
    #     num_epochs_per_stage.append(len(epochs))
    #
    # # 绘制曲线
    # plt.plot(all_epochs, all_losses)
    # plt.xlabel('Epoch')
    # plt.ylabel('Loss')
    # plt.title('Loss Curve')
    #
    # # 在各个阶段之间绘制绿色竖直虚线和标记
    # for i in range(1, len(file_paths)):
    #     epoch_boundary = all_epochs[sum(num_epochs_per_stage[:i]) - 1]
    #     plt.axvline(x=epoch_boundary, color='g', linestyle='--')
    #     plt.text(epoch_boundary, min(all_losses), f'Stage {i}', va='bottom', ha='left')
    #
    # plt.show()
    all_epochs = []
    all_losses = []
    num_epochs_per_stage = []
    min_points = []

    for file_path in file_paths:
        # 读取文件内容
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # 使用正则表达式匹配包含'loss'的行并捕获数据
        pattern = re.compile(
            r"\'loss\':\s*(\d+\.\d+),\s*\'grad_norm\':\s*\d+\.\d+,\s*\'learning_rate\':\s*\d+\.\d+,\s*\'epoch\':\s*(\d+\.\d+)")
        data = [match.groups() for line in lines for match in [pattern.search(line)] if match]

        # 转换数据为浮点数并提取epoch和loss数据
        epochs = [float(d[1]) for d in data]
        losses = [float(d[0]) for d in data]

        # 如果不是第一个阶段，将横轴偏移
        if all_epochs:
            epoch_offset = all_epochs[-1]
            epochs = [epoch + epoch_offset for epoch in epochs]

        # 将当前阶段的数据添加到总数据中
        all_epochs.extend(epochs)
        all_losses.extend(losses)
        num_epochs_per_stage.append(len(epochs))

        # 找到当前阶段的最低点
        min_index = losses.index(min(losses))
        min_epoch = epochs[min_index]
        min_loss = losses[min_index]
        min_points.append((min_epoch, min_loss))

    # 绘制曲线
    plt.plot(all_epochs, all_losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss Curve')

    # 在各个阶段之间绘制绿色竖直虚线和标记
    for i in range(1, len(file_paths)):
        epoch_boundary = all_epochs[sum(num_epochs_per_stage[:i]) - 1]
        plt.axvline(x=epoch_boundary, color='g', linestyle='--')
        plt.text(epoch_boundary, min(all_losses), f'Stage {i}', va='bottom', ha='left')

    # 绘制每个阶段的最低点直线
    for min_epoch, min_loss in min_points:
        plt.axvline(x=min_epoch, color='r', linestyle='--')
        plt.axhline(y=min_loss, color='r', linestyle='--')
        plt.text(min_epoch, min_loss, f'Min Loss: {min_loss:.4f}', va='bottom', ha='left')

    plt.show()


if __name__ == '__main__':
    # 调用函数
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mgm_2b_loss.txt'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/mgm_finetune_loss.txt'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/pretrain.txt'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0818/pretrain.log'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0818/finetuning.log'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0821/pretrain.log'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0821/finetuning.log'
    # file_path = '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/pretrain.log'
    # plot_loss_curve(file_path)

    # 调用函数
    # file_paths = ['/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0821/pretrain.log',
    #               '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0821/finetuning.log']
    # file_paths = ['/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0818/pretrain.log',
    #               '/Users/gatilin/PycharmProjects/model-metrics-plot/data/loss/0818/finetuning.log']
    file_paths = ['/Users/gatilin/PycharmProjects/model-metrics-plot/data/pretrain.txt',
                  '/Users/gatilin/PycharmProjects/model-metrics-plot/data/finetuning.log']
    plot_mult_loss_curve(file_paths)