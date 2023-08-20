
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

# 读取 csv 文件
df = pd.read_csv('../data/data1.csv')

# 饼图
plt.pie(df['value'], labels=df['category'], autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# 条形图
sns.barplot(x='value', y='category', data=df)
plt.title('Bar Chart')
plt.show()

# 区域图
sns.lineplot(x='date', y='value', hue='category', data=df)
plt.fill_between(df['date'], df['value'], alpha=0.2)
plt.title('Area Chart')
plt.show()

# 树状图
G = nx.DiGraph()
G.add_edges_from(df[['parent', 'child']].values)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
nx.draw_networkx_labels(G, pos)
plt.title('Tree Chart')
plt.show()

# 网络图
G = nx.karate_club_graph()
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.title('Network Chart')
plt.show()

# 密度图
sns.kdeplot(df['value'], fill=True)
plt.title('Density Chart')
plt.show()

# 箱形图
sns.boxplot(x='category', y='value', data=df)
plt.title('Box Chart')
plt.show()

# 热图
pivot_table = df.pivot_table(index='category', columns='date', values='value')
sns.heatmap(pivot_table, cmap='YlGnBu')
plt.title('Heatmap')
plt.show()