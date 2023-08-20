import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.tree import DecisionTreeClassifier, plot_tree

def plot_bubble_chart(df, x_col, y_col, value_col):
    """
    绘制气泡图

    参数：
    df：DataFrame，数据集
    x_col：str，x 轴所用的列名
    y_col：str，y 轴所用的列名
    value_col：str，气泡大小所用的列名

    返回值：
    无
    """
    plt.scatter(df[x_col], df[y_col], s=df[value_col])
    plt.title('Bubble Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [4, 5, 6, 7, 8, 9],
    'value': [10, 20, 30, 15, 25, 35]
})
plot_bubble_chart(df, 'x', 'y', 'value')

def plot_matrix_chart(df):
    """
    绘制矩阵图

    参数：
    df：DataFrame，数据集

    返回值：
    无
    """
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
    plt.title('Matrix Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [4, 5, 6, 7, 8, 9],
    'value': [10, 20, 30, 15, 25, 35]
})
plot_matrix_chart(df)

def plot_3d_scatter_chart(df, x_col, y_col, value_col):
    """
    绘制三维散点图

    参数：
    df：DataFrame，数据集
    x_col：str，x 轴所用的列名
    y_col：str，y 轴所用的列名
    value_col：str，z 轴所用的列名

    返回值：
    无
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x_col], df[y_col], df[value_col])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Value Label')
    plt.title('3D Scatter Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [4, 5, 6, 7, 8, 9],
    'value': [10, 20, 30, 15, 25, 35]
})
plot_3d_scatter_chart(df, 'x', 'y', 'value')

# def plot_spider_chart(df, category_col, value_col):
#     """
#     绘制蜘蛛图
#
#     参数：
#     df：DataFrame，数据集
#     category_col：str，分类所用的列名
#     value_col：str，值所用的列名
#
#     返回值：
#     无
#     """
#     categories = df[category_col].unique()
#     values = df.groupby(category_col)[value_col].sum().values
#     angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
#     values = np.concatenate((values,[values[0]]))
#     angles = np.concatenate((angles,[angles[0]]))
#     fig = plt.figure()
#     ax = fig.add_subplot(111, polar=True)
#     ax.plot(angles, values, 'o-', linewidth=2)
#     ax.fill(angles, values, alpha=0.25)
#     ax.set_thetagrids(angles * 180/np.pi, categories)
#     plt.title('Spider Chart')
#     plt.show()
#
# # 示例数据
# # df = pd.DataFrame({
# #     'category': ['A', 'A', 'A', 'B', 'B', 'B'],
# #     'value': [10, 20, 30, 15, 25, 35]
# # })
#
# # 蜘蛛图示例数据
# df = pd.DataFrame({
#     'category': ['A', 'A', 'A', 'B', 'B', 'B'],
#     'value': [10, 20, 30, 15, 25, 35]
# })
#
# plot_spider_chart(df, 'category', 'value')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_spider_chart(df, category_col, value_col):
    """
    绘制蜘蛛图

    参数：
    df：DataFrame，数据集
    category_col：str，分类所用的列名
    value_col：str，值所用的列名

    返回值：
    无
    """
    categories = df[category_col].unique()
    values = df.groupby(category_col)[value_col].sum().values
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values,[values[0]]))
    angles = np.concatenate((angles,[angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title('Spider Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'value': [10, 20, 30, 15, 25, 35]
})
plot_spider_chart(df, 'category', 'value')

def plot_rose_chart(df, category_col, value_col):
    """
    绘制玫瑰图

    参数：
    df：DataFrame，数据集
    category_col：str，分类所用的列名
    value_col：str，值所用的列名

    返回值：
    无
    """
    theta = np.linspace(0, 2*np.pi, len(df[category_col]), endpoint=False)
    radii = df[value_col].values
    width = np.pi/4
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    for r, bar in zip(radii, bars):
        bar.set_alpha(0.5)
        bar.set_facecolor(plt.cm.jet(r/10.))
    plt.title('Rose Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'value': [10, 20, 30, 40]
})
plot_rose_chart(df, 'category', 'value')

def plot_radar_chart(df, category_col, value_col):
    """
    绘制雷达图

    参数：
    df：DataFrame，数据集
    category_col：str，分类所用的列名
    value_col：str，值所用的列名

    返回值：
    无
    """
    categories = df[category_col].unique()
    values = df.groupby(category_col)[value_col].sum().values
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values,[values[0]]))
    angles = np.concatenate((angles,[angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    # ax.set_thetagrids(angles * 180/np.pi, categories)
    # 设置刻度、标签和标题
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title('Radar Chart')
    plt.show()

# 示例数据
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B'],
    'value': [10, 20, 30, 40]
})
plot_radar_chart(df, 'category', 'value')