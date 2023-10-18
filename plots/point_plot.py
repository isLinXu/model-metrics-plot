import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.data = pd.read_csv(data_file_path)

    def scatter_plot(self):
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))

        sns.scatterplot(data=self.data, x="x", y="y", marker="o", color="b", label="Data Points")

        plt.title("Scatter Plot using Seaborn")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.show()

    def linear_regression_plot(self):
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))

        sns.regplot(data=self.data, x="x", y="y", scatter_kws={"color": "blue"}, line_kws={"color": "red"})

        plt.title("Linear Regression Plot using Seaborn")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()

    def histogram_plot(self):
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))

        sns.histplot(data=self.data, x="x", bins=10, color="green", kde=True)

        plt.title("Histogram using Seaborn")
        plt.xlabel("X-axis")
        plt.ylabel("Frequency")
        plt.show()

if __name__ == '__main__':
    plotting = Plotting("../data/data.csv")
    plotting.scatter_plot()
    plotting.linear_regression_plot()
    plotting.histogram_plot()