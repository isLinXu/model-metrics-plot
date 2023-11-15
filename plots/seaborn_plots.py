import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier, plot_tree

class DataVisualization:
    def __init__(self, data_file):
        self.df = pd.read_csv(data_file)

    def bubble_chart(self):
        plt.scatter(self.df['x'], self.df['y'], s=self.df['value'])
        plt.title('Bubble Chart')
        plt.show()

    def matrix_chart(self):
        corr_matrix = self.df.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
        plt.title('Matrix Chart')
        plt.show()

    def scatter_3d_chart(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.df['x'], self.df['y'], self.df['value'])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Value Label')
        plt.title('3D Scatter Chart')
        plt.show()

    def spider_chart(self):
        categories = self.df['category'].unique()
        values = self.df.groupby('category')['value'].sum().values
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
        values = np.concatenate((values,[values[0]]))
        angles = np.concatenate((angles,[angles[0]]))
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, categories)
        plt.title('Spider Chart')
        plt.show()

    def rose_chart(self):
        theta = np.linspace(0, 2*np.pi, len(self.df['category']), endpoint=False)
        radii = self.df['value'].values
        width = np.pi/4
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        bars = ax.bar(theta, radii, width=width, bottom=0.0)
        for r, bar in zip(radii, bars):
            bar.set_alpha(0.5)
            bar.set_facecolor(plt.cm.jet(r/10.))
        plt.title('Rose Chart')
        plt.show()

    def radar_chart(self):
        categories = self.df['category'].unique()
        values = self.df.groupby('category')['value'].sum().values
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
        values = np.concatenate((values,[values[0]]))
        angles = np.concatenate((angles,[angles[0]]))
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, categories)
        plt.title('Radar Chart')
        plt.show()

    def forest_chart(self):
        X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=0)
        clf = DecisionTreeClassifier(random_state=0)
        clf.fit(X, y)
        plt.figure()
        plot_tree(clf, filled=True)
        plt.title('Forest Chart')
        plt.show()

    def histogram(self, column, bins=10):
        plt.hist(self.df[column], bins=bins)
        plt.title('Histogram')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def box_plot(self, column):
        sns.boxplot(x=self.df[column])
        plt.title('Box Plot')
        plt.xlabel(column)
        plt.show()

    def violin_plot(self, column, category):
        sns.violinplot(x=category, y=column, data=self.df)
        plt.title('Violin Plot')
        plt.xlabel(category)
        plt.ylabel(column)
        plt.show()

    def bar_chart(self, category, value):
        sns.barplot(x=category, y=value, data=self.df)
        plt.title('Bar Chart')
        plt.xlabel(category)
        plt.ylabel(value)
        plt.show()

    def pie_chart(self, column):
        values = self.df[column].value_counts().values
        labels = self.df[column].value_counts().index
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title('Pie Chart')
        plt.show()

    def dual_axis_chart(self, column1, column2):
        fig, ax1 = plt.subplots()
        ax1.plot(self.df[column1], 'b-')
        ax1.set_xlabel('Index')
        ax1.set_ylabel(column1, color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(self.df[column2], 'r-')
        ax2.set_ylabel(column2, color='r')
        ax2.tick_params('y', colors='r')

        plt.title('Dual Axis Chart')
        plt.show()


if __name__ == '__main__':
    data_visualization = DataVisualization('../data/data2.csv')
    data_visualization.bubble_chart()
    data_visualization.matrix_chart()
    data_visualization.scatter_3d_chart()
    # data_visualization.spider_chart()
    data_visualization.rose_chart()
    # data_visualization.radar_chart()
    data_visualization.forest_chart()